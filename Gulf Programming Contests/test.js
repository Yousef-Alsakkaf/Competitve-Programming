import * as p from '@clack/prompts';
import { spinner } from '@clack/prompts';
import color from 'picocolors';
import * as fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { execFile, spawn } from 'child_process';
import os from 'os'
const loading = spinner();
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const processArguments = process.argv;
let yearToTest;
let examToTest;
let pythonCommand = os.platform() === 'darwin' ? 'python3' : 'python';

let argumentsFlags = {
    hideAnswers: false,
    hideStats: false,
    showFullStats: false
}

if (processArguments.length == 2) {
    p.intro(`${color.bgRed(color.green(' Please supply arguments -y '))}`);
    process.exit(0);
}

if (processArguments[2] == "-y" && processArguments[3] != undefined) {
    yearToTest = processArguments[3];
}

if (processArguments[4] == "-n" && processArguments[5] != undefined) {
    examToTest = processArguments[5];
} else {
    p.intro(`${color.bgCyan(color.black(' Undefined error occured '))}`);
}

if (processArguments.includes("--hide-answers")) {
    argumentsFlags["hideAnswers"] = true;
}

if (processArguments.includes("--hide-stats")) {
    argumentsFlags["hideStats"] = true;
}
 
if (processArguments.includes("--show-full-stats")) {
    argumentsFlags["showFullStats"] = true;
}

p.intro(`${color.bgMagenta(color.black(' Testing '))} ${color.bgRed(color.green(yearToTest))}`);

const directoryPath = path.join(__dirname, yearToTest, examToTest);
let isSourceCode = false;
let isInputFile = false;
let isOutputFile = false;

// Check if the directory exists
if (fs.existsSync(directoryPath)) {
    // Get a list of files in the directory
    const files = fs.readdirSync(directoryPath);

    // Iterate through the files
    files.forEach(fileName => {
        const fileExtension = path.extname(fileName);

        // Check if the file extension is in the list of allowed extensions
        if (fileExtension.includes(fileExtension)) {
            const filePath = path.join(directoryPath, fileName);

            // Check if the file exists
            if (fs.existsSync(filePath)) {
                if (fileExtension === '.in') {
                    isInputFile = true;
                } else if (fileExtension === '.out') {
                    isOutputFile = filePath;
                } else if ((fileExtension === '.java' || fileExtension === '.py') && !isSourceCode) {
                    isSourceCode = { extention: fileExtension === '.java' ? 'Java' : 'Python', path: filePath };
                }
            }
        }
    });

    if (!isInputFile) {
        p.outro(color.bgRed("No input file detected"))
    } else if (!isOutputFile) {
        p.outro(color.bgRed("No output file detected"))
    } else if (!isSourceCode) {
        p.outro(color.bgRed("No source code detected"))
        process.exit(0);
    } else {
        loading.start("Source code detected: " + color.bgGreen(`${isSourceCode.extention}`));
        loading.stop("Source code detected: " + color.bgGreen(`${isSourceCode.extention}`));
    }
} else {
    p.outro(color.bgRed("Directory doesn't exist!"))
    process.exit(0);
}

loading.start('Running ' + color.bgCyan(path.basename(isSourceCode.path)));

runJavaOrPythonFile(isSourceCode.path).then((result) => {
    loading.stop('Running ' + color.bgCyan(path.basename(isSourceCode.path)));
    result.output = result.output.substring(0, 70);;
    if(!argumentsFlags["hideStats"]) {
        p.note(`Time complexity: ${color.bgYellow(result.elapsedTime)} ms\nSpace complexity: ${color.bgMagenta(result.spaceComplexity)} MB \nOutput: ${result.output}`);
        p.outro(color.bgGreen("Test complete"));
    } else if(argumentsFlags["showFullStats"]) {
        // Add more stats
    } else {
        p.note("You can remove --hide-answers to view your answers");
    }
    compareOutputs()
}).catch((error) => {
    p.note(error.message)
    loading.stop('Running ' + color.bgCyan(path.basename(isSourceCode.path)));
    p.outro("Error while compiling or running the source code")
})

function compareOutputs() {
    const file = findFileByExtension(directoryPath, 'answer');
    if (!file) {
        p.outro(color.bgRed("No answer file detected"))
        process.exit(0);
    }

    loading.start('Checking answer ' + path.basename(file));
    const check = compareFiles(file, isOutputFile)
    loading.stop('Checking answer ' + path.basename(file));

    if (check.areIdentical) {
        p.outro(color.bgGreen("Test complete success"));
    } else {
        let stringNote = "";
        if(!argumentsFlags["hideAnswers"]) {
            if (check.numDifferences > 0) {
                stringNote += `${color.bgRed(check.numDifferences + " case(s) have not been handled")}\n`;
            } else if (check.differentLines > 0) {
                stringNote += `${color.bgRed(check.differentLines)} case(s) are wrong\n\n`;
                stringNote += `${color.bgRed(`Your answer: ${check.line1}`)}\n${color.bgGreen(`Correct answer: ${check.line2}`)}\n`;
            }
        } else {
            stringNote += `${("You can remove --hide-answers to view your answers")}`;
        }
        p.note(stringNote)
        p.outro(color.bgRed("Test complete failed"));
    };
}

function runJavaOrPythonFile(filePath) {
    return new Promise((resolve, reject) => {
        const extension = filePath.split('.').pop();
        const startTime = process.hrtime();
        const currentSpace = process.memoryUsage().heapUsed;
        const options = {
            cwd: directoryPath,
        };

        if (extension === 'java') {
            execFile('java', [filePath], options, (error, stdout, stderr) => {
                if (error) {
                    reject(error);
                } else {
                    console.log(filePath)
                    execFile('java', [filePath], options, (error, stdout, stderr) => {
                        if (error) {
                            reject(error);
                        } else {
                            const elapsedTime = process.hrtime(startTime);
                            console.log(stdout)
                            resolve({
                                output: stdout.trim(),
                                elapsedTime: Math.ceil((elapsedTime[0] * 1e9 + elapsedTime[1]) / 1e6), // in nanoseconds
                                spaceComplexity: Math.ceil((process.memoryUsage().heapUsed - currentSpace) / 1024 / 1024) // Python's memory usage is more complex to measure
                            });
                        }
                    });
                }
            });
        } else if (extension === 'py') {


            execFile(pythonCommand, [filePath], options, (error, stdout, stderr) => {

                if (error) {
                    reject(error);
                } else {
                    const elapsedTime = process.hrtime(startTime);
                    resolve({
                        output: stdout.trim(),
                        elapsedTime: Math.ceil((elapsedTime[0] * 1e9 + elapsedTime[1]) / 1e6),
                        spaceComplexity: Math.ceil((process.memoryUsage().heapUsed - currentSpace) / 1024 / 1024)
                    });
                }
            });
        } else {
            reject(new Error('Unsupported file extension. Only .java and .py files are supported.'));
        }
    });
}

function compareFiles(file1, file2) {
    const content1 = fs.readFileSync(file1, 'utf-8');
    const content2 = fs.readFileSync(file2, 'utf-8');
    let counterOfErrors = 0;
    let firstError = [];
    let firstErrorBool = false;

    if (content1 === content2) {
        return { areIdentical: true };
    } else {
        const lines1 = content1.split('\n');
        const lines2 = content2.split('\n');
        const diffCount = Math.max(lines1.length, lines2.length);

        for (let i = 0; i < diffCount; i++) {
            if (lines1[i] !== lines2[i]) {
                counterOfErrors++;

                if (!firstErrorBool) {
                    firstError = [lines1[i], lines2[i]];
                    firstErrorBool = true;
                }
            }
        }

        return {
            areIdentical: false,
            numDifferences: Math.abs(lines1.length - lines2.length),
            differentLines: counterOfErrors,
            line1: firstError[0],
            line2: firstError[1]
        };
    }
}

function findFileByExtension(directory, extension) {
    const files = fs.readdirSync(directory);

    for (const file of files) {
        const filePath = path.join(directory, file);
        const stats = fs.statSync(filePath);

        if (stats.isFile() && path.extname(file) === `.${extension}`) {
            return filePath;
        }
    }

    return false;
}