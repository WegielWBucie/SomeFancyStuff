public class Heap {

    protected int [] heapData;
    protected int sizeOfHeap;
    protected final int heapMaxSize;

    protected static final int FRONT = 1;


    public Heap(int heapMaxSize) {
        this.heapMaxSize = heapMaxSize;
        this.sizeOfHeap = 0;
        heapData = new int[this.heapMaxSize + 1];
    }

    public int getHeapMaxSize() {
        return heapMaxSize;
    }
    protected int getSizeOfHeap() {
        return this.sizeOfHeap;
    }

    protected int getParentPosition(int position) {
        return position / 2;
    }
    protected int getLeftChildPosition(int position) {
        return 2 * position;
    }
    protected int getRightChildPosition(int position) {
        return 2 * position + 1;
    }

    protected boolean notLeaf(int position) {
        return position < (sizeOfHeap / 2) || position > sizeOfHeap;
    }

    protected void swapNodes(int firstNode, int secondNode) {
        //swap without temporary variable
        heapData[firstNode] = heapData[firstNode] + heapData[secondNode];
        heapData[secondNode] = heapData[firstNode] - heapData[secondNode];
        heapData[firstNode] = heapData[firstNode] - heapData[secondNode];
    }

    public void displayHeap() {
        System.out.print("Parent Node:" + "\t" + "Left Child Node:" + "\t");
        System.out.println("Right Child Node:");
        for(int i = 1; i <= ((sizeOfHeap - 1) / 2); i++) {
            System.out.println(heapData[i] + "\t\t\t\t" + heapData[2 * i] + "\t\t\t\t\t" + heapData[2 * i + 1]);
            System.out.println();
        }
    }

    protected void insertNode(int value) {
        if(this.sizeOfHeap >= this.heapMaxSize) return;
        heapData[++sizeOfHeap] = value;
    }

    protected int popElement() {
        int element = heapData[FRONT];
        heapData[FRONT] = heapData[sizeOfHeap--];
        return element;
    }
}


