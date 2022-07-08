public class MinHeap extends Heap {

    public MinHeap(int heapMaxSize) {
        super(heapMaxSize);
        super.heapData[0] = Integer.MIN_VALUE;
    }

    private void minHeapify(int position) {
        if(super.notLeaf(position)) {
            if(heapData[position] > heapData[getLeftChildPosition(position)] ||
                    heapData[position] > heapData[getRightChildPosition(position)]) {

                if(heapData[getLeftChildPosition(position)] < heapData[getRightChildPosition(position)]) {
                    swapNodes(position, getLeftChildPosition(position));
                    minHeapify(getLeftChildPosition(position));
                }
                else {
                    swapNodes(position, getRightChildPosition(position));
                    minHeapify(getRightChildPosition(position));
                }
            }
        }
    }

    public void designMinHeap() {
        for(int position = sizeOfHeap / 2; position >= 1; position--) {
            minHeapify(position);
        }
    }

    public void insertNode(int value) {
        super.insertNode(value);
        int currentSize = sizeOfHeap;
        while(heapData[currentSize] < heapData[getParentPosition(currentSize)]) {
            swapNodes(currentSize, getParentPosition(currentSize));
        }
    }

    public int pop() {
        minHeapify(FRONT);
        return super.popElement();
    }
}
