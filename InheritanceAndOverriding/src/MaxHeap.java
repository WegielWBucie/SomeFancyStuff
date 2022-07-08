public class MaxHeap extends Heap {

    public MaxHeap(int heapMaxSize) {
        super(heapMaxSize);
        super.heapData[0] = Integer.MAX_VALUE;
    }

    private void maxHeapify(int position) {
        if(super.notLeaf(position)) {
            if(heapData[position] < heapData[getLeftChildPosition(position)] ||
               heapData[position] < heapData[getRightChildPosition(position)]) {

                if(heapData[getLeftChildPosition(position)] > heapData[getRightChildPosition(position)]) {
                    super.swapNodes(position, getLeftChildPosition(position));
                    maxHeapify(getLeftChildPosition(position));
                }
                else {
                    super.swapNodes(position, getRightChildPosition(position));
                    maxHeapify(getRightChildPosition(position));
                }
            }
        }
    }

    public void designMaxHeap() {
        for(int position = sizeOfHeap / 2; position >= 1; position--) {
            maxHeapify(position);
        }
    }

    public void insertNode(int data) {
        super.insertNode(data);
        while(heapData[sizeOfHeap] > heapData[getParentPosition(sizeOfHeap)]) {
            super.swapNodes(sizeOfHeap, getParentPosition(sizeOfHeap));
        }
    }

    public int pop() {
        maxHeapify(FRONT);
        return super.popElement();
    }
}