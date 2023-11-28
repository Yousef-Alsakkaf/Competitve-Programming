import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

class main {
    public static void main(String[] args) throws IOException{
        BufferedReader file = new BufferedReader(new FileReader("bridges.in"));
        String line = file.readLine();
        int numberOfCases = Integer.parseInt(line);

        for(int i = 0; i < numberOfCases; i++) {
            int numberOfPedestrians = Integer.parseInt(file.readLine());
            ArrayList<ArrayList<Integer>> arrivingMap = new ArrayList<ArrayList<Integer>>();
            ArrayList<Integer> trackTimeMap = new ArrayList<Integer>();
            int counter = 0;
            int maxNumOfPassengers = 0;

            for(int j = 0; j < numberOfPedestrians; j++) {
                String[] arguments = file.readLine().split(" ");
                int arrivingTime = Integer.parseInt(arguments[0]);
                int finishTime = Integer.parseInt(arguments[1]);
                ArrayList<Integer> array = new ArrayList<Integer>();
                array.add(arrivingTime);
                array.add(finishTime);
                arrivingMap.add(array);
            }

            while(!arrivingMap.isEmpty()) {
                boolean hasReachedNumber = false;

                for(int a = 0; a < arrivingMap.size(); a++) {
                    ArrayList<Integer> value = arrivingMap.get(a);

                    if(!hasReachedNumber && counter == a) {
                        trackTimeMap.add(value.get(0) + value.get(1));
                        hasReachedNumber = true;
                    } else if(hasReachedNumber && counter != a) {
                        if(trackTimeMap.get(a) >= counter) {
                            trackTimeMap.remove(a);
                        }
                        break;
                    }

                    if(maxNumOfPassengers < arrivingMap.size()) {
                        maxNumOfPassengers = arrivingMap.size();
                    }
                }

                counter++;
            }

            System.out.println(maxNumOfPassengers);
        }
    }
}

// [[1, 2], [3, 4]]
// Counter 0, []
// Counter 1, [person1]
// Counter 2, [person1]
// Counter 3, [person1, person2]
// Counter 4, [person2]
// Counter 5, [person2]
// Counter 6, [person2]
// Counter 7, [person2]