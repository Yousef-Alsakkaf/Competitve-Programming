#include <iostream>
#include <vector>
#include<string>
#include <fstream>
using namespace std;

class Movie {
public:
    //Attributes
    string title;
    short int releaseYear;
    string director;
    string category;
    float imdb; //IMDB Rating
    short int runtime; //in mins
    int MovieID;
    string desc; //Description
    Movie* next;


    Movie(const string& title, short int releaseYear, const string& director, const string& category, float imdb, short int runtime, int MovieID, const string& desc) {
        this->title = title;
        this->releaseYear = releaseYear;
        this->director = director;
        this->category = category;
        this->imdb = imdb;
        this->runtime = runtime;
        this->MovieID = MovieID;
        this->desc = desc;
        this->next = nullptr;
    }

    Movie(){}

};

class LinkedList {
    string listName;
    Movie* head;
    


public:
    LinkedList(string listName) {
        this->listName = listName;
        head = nullptr;
    }

    void isEmpty() {
        if (head == nullptr) {
            cout << "List is empty!" << endl;
        }
        else {
            int short numOfMovies = 0;
            Movie* curr = head;
            while (curr) {
                curr = curr->next;
                numOfMovies++;
            }
            cout << "List has " << numOfMovies << " moveis"<<endl;
        }
            
    }

    void addNewMovie(const string& title, short int releaseYear, const string& director, const string& category, float imdb, short int runtime, int MovieID, const string& desc) {
        Movie* newMovie = new Movie(title, releaseYear, director, category, imdb, runtime, MovieID, desc);
        if (!head)
            head = newMovie;
        else {
            Movie* currentMovie = head;
            while (currentMovie->next)
                currentMovie = currentMovie->next; //Iterate until the last movie

            currentMovie->next = newMovie;
        }
    }

    void insertMovie(const string& title, short int releaseYear, const string& director, const string& category,
        float imdb, short int runtime, int MovieID, const string& desc, int p) {
        Movie* newMovie = new Movie(title, releaseYear, director, category, imdb, runtime, MovieID, desc);
        if (head == NULL && p != 0) {
            cout << "List is empty!" << endl;
            delete newMovie;
            return;
        }
        else if (head == NULL && p == 0) {
            head = newMovie;
            return;
        }
        else if (head != NULL && p == 0) {
            newMovie->next = head;
            head = newMovie;
            return;
        }
        else {
            Movie* curr = head;
            int i = 0;

            while (i < p - 1) {
                if (curr->next == NULL || p < 0) {
                    cout << "invalid position" << endl;
                    delete newMovie;
                    return;
                }
                curr = curr->next;
                i++;


            }
            newMovie->next = curr->next;
            curr->next = newMovie;
            return;
        }

    }

    void displayAllMovie() {
        Movie* currentMovie = head;
        int short numOfMovies = 0;
        if (head == nullptr)
            cout << "LIST IS EMPTY" << endl;

        while (currentMovie) {
            cout << "Movie #" << (numOfMovies + 1) << endl;
            cout << "Movie Title: " << currentMovie->title << endl;
            cout << "Released in: " << currentMovie->releaseYear << endl;
            cout << "Director: " << currentMovie->director << endl;
            cout << "Category: " << currentMovie->category << endl;
            cout << "IMDB Rating: " << currentMovie->imdb << endl;
            cout << "Runtime: " << currentMovie->runtime << " minutes" << endl;
            cout << "Movie ID: " << currentMovie->MovieID << endl;
            cout << "Description: " << currentMovie->desc << endl;
            cout << "----------------------------------------"<< endl;
            numOfMovies++;

            currentMovie = currentMovie->next;
        }
        if (numOfMovies == 1)
            cout << "There is " << numOfMovies << " movie in your " << listName << " list" << endl;
        else
            cout << "There are " << numOfMovies << " movies in your " << listName << " list" << endl;
        cout << "========================================" << endl;


    }

    void findByID(int ID) {

        if (head == NULL) {
            cout << "List is empty" << endl;
            return;
        }

        else {
            Movie* curr = head;
            Movie* prev = nullptr;
            while (ID != curr->MovieID) {
                if (curr->next == NULL) {
                    cout << "Movie Not found" << endl;
                    return;
                }                
                curr = curr->next;

            }

            
            cout << "Movie Title" << curr->title << endl;
            cout << "Released in: " << curr->releaseYear << endl;
            cout << "Director: " << curr->director << endl;
            cout << "Category: " << curr->category << endl;
            cout << "IMDB Rating: " << curr->imdb << endl;
            cout << "Runtime: " << curr->runtime << " minutes" << endl;
            cout << "Movie ID: " << curr->MovieID << endl;
            cout << "Description: " << curr->desc << endl;
            cout << "----------------------------------------" << endl;

        }

        return;
    }
    void deleteAll() {
        Movie* currentMovie = head;

        while (currentMovie) {
            Movie* temp = currentMovie;
            currentMovie = currentMovie->next;
            delete temp;
        }

        head = nullptr;
    }

    

    void deleteByID( int ID) {

        if (head == NULL) {
            cout << "List is empty" << endl;
            return;
        }
        
        else {
            Movie* curr = head;
            Movie* prev=nullptr;
            while (ID!=curr->MovieID) {
                if (curr->next == NULL) {
                    cout << "Movie Not found" << endl;
                    return;
                }
                prev = curr;
                curr = curr->next;
                


            }
            
            prev->next = curr->next;
            delete curr;

        }

        return;
    }

    

    void save() {
        ofstream outputFile(listName + ".txt"); // Append ".txt" to the filename
        if (!(outputFile.is_open()))
            createFile();

        if (outputFile.is_open()) {
            Movie* currentMovie = head;
            while (currentMovie) {
                // Write each movie's data to the file in a text format
                outputFile << currentMovie->title << "\n";
                outputFile << currentMovie->releaseYear << "\n";
                outputFile << currentMovie->director << "\n";
                outputFile << currentMovie->category << "\n";
                outputFile << currentMovie->imdb << "\n";
                outputFile << currentMovie->runtime << "\n";
                outputFile << currentMovie->MovieID << "\n";
                outputFile << currentMovie->desc << "\n";
                

                currentMovie = currentMovie->next;
            }

            outputFile.close();
            cout << "Data has been saved to '" << listName << ".txt'." << endl;
        }
        else {
            cerr << "Failed to create or open the file for saving data." << endl;
        }
    }

    void load() {
        ifstream inputFile(listName + ".txt");

        if (inputFile.is_open()) {
            Movie movie;
            string line;

            while (getline(inputFile, line)) {

                movie.title = line;
                if (getline(inputFile, line)) {
                    movie.releaseYear = stoi(line);
                }
                else {
                    cerr << "Error: Invalid data format for releaseYear." << endl;
                    break;
                }

                // Continue to read and populate other movie attributes
                if (getline(inputFile, line)) {
                    movie.director = line;
                }
                else {
                    cerr << "Error: Invalid data format for director." << endl;
                    break;
                }

                if (getline(inputFile, line)) {
                    movie.category = line;
                }
                else {
                    cerr << "Error: Invalid data format for category." << endl;
                    break;
                }

                if (getline(inputFile, line)) {
                    movie.imdb = stof(line);
                }
                else {
                    cerr << "Error: Invalid data format for imdb." << endl;
                    break;
                }

                if (getline(inputFile, line)) {
                    movie.runtime = stoi(line);
                }
                else {
                    cerr << "Error: Invalid data format for runtime." << endl;
                    break;
                }

                if (getline(inputFile, line)) {
                    movie.MovieID = stoi(line);
                }
                else {
                    cerr << "Error: Invalid data format for MovieID." << endl;
                    break;
                }

                if (getline(inputFile, line)) {
                    movie.desc = line;
                }
                else {
                    cerr << "Error: Invalid data format for desc." << endl;
                    break;
                }

                // Add the movie to the linked list
                addNewMovie(movie.title, movie.releaseYear, movie.director, movie.category, movie.imdb, movie.runtime, movie.MovieID, movie.desc);
            }

            inputFile.close();
            cout << "Data has been loaded from '" << listName << ".txt'." << endl;
        }
        else {
            cerr << "Failed to open the file for loading data." << endl;
        }
    }


    void createFile() {
        ofstream outputFile(listName);

        if (outputFile.is_open()) {
            outputFile.close();
            cout << "File '" << listName << "' has been created." << endl;
        }
        else {
            cerr << "Failed to create the file '" << listName << "'." << endl;
        }
    }

      
};

int main() {
    vector <LinkedList> allMovies;

    cout << "Create New List? (yes/no) " << endl;
    string answer;
    cin >> answer;
    cin.ignore(); //to ignore all left overs and not skip the next line
    if (answer == "yes") {
        string listName;
        cout << "Please enter your list's name: " << endl; //Adding new list
        getline(cin, listName); //to take more than 1 name incase provided
        LinkedList newListofMovies(listName);   
        newListofMovies.addNewMovie("Maze Runner", 2020, "Yamanos Silva", "Horror", 9.9f, 95, 22001064,
            "Best Movie Ever"); //Adding new node
        newListofMovies.addNewMovie("Maze Runner1", 2023, "Yamanosh Shilva", "Comedy", 9.8f, 94, 22001065,
            "Best Movieee Everrr"); //Adding new node
        newListofMovies.displayAllMovie();
        newListofMovies.insertMovie("Interstellar", 2014, "Christopher Nolan", "Sci-fi", 8.7f, 168, 22000234, "guy go space", 1);
        newListofMovies.save();

      
       
        allMovies.push_back(newListofMovies);

    }
    else
        cout << "How Can CornFlix Help You?" << endl;


    return 0;
}
