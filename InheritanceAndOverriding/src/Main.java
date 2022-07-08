import java.util.Random;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("Heap size: ");
        int heapSize;
        heapSize = scanner.nextInt();

        Random random = new Random();

        MinHeap minHeap = new MinHeap(heapSize);

        for(int i = 1; i <= heapSize; i++) {
            minHeap.insertNode(random.nextInt(0, 100));
        }
        minHeap.designMinHeap();
        minHeap.displayHeap();


        MaxHeap maxHeap = new MaxHeap(heapSize);
        for(int i = 1; i <= heapSize; i++) {
            maxHeap.insertNode(random.nextInt(0, 100));
        }
        maxHeap.designMaxHeap();
        maxHeap.displayHeap();
    }
}
