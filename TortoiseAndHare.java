class Node {
	int  data;
	Node next;

	Node(int d) {
		this.data = d;
		this.next = null;
	}
}

public class TortoiseAndHare {
	public Node head = null;
	public Node last;
	Node        slow_p, fast_p;
	int         startingIndex, endingIndex;
	public void push(int new_data) {
		Node new_node = new Node(new_data);
		if (this.head == null) {
			this.last = new_node;
		}
		new_node.next = this.head;
		this.head = new_node;
	}

	private boolean detectLoop() {
		this.slow_p = this.head;
		this.fast_p = this.head;
		while ((this.slow_p != null) && (this.fast_p != null) && (this.fast_p.next != null)) {
			this.slow_p = this.slow_p.next;
			this.fast_p = this.fast_p.next.next;
			if (this.slow_p == this.fast_p) {
				return true;
			}
		}
		return false;
	}

	public static void main(String args[]) {
		TortoiseAndHare llist = new TortoiseAndHare();

		llist.push(1);
		llist.push(2);
		llist.push(3);
		llist.push(4);
		llist.push(5);
		llist.push(6);
		llist.push(7);

		llist.head.next.next.next.next.next = llist.head.next;

		if(llist.detectLoop()) {
			System.out.println("Loop Detected");
			llist.findStartOfLoop();
			llist.findEndOfLoop();
			System.out.println("Starting index of loop:" + llist.startingIndex);
			System.out.println("Ending index of loop:" + llist.endingIndex);
		}
	}
	
	private void findEndOfLoop() {
		this.fast_p        = this.slow_p.next;
		this.endingIndex   = this.startingIndex + 1;
		while (this.slow_p != this.fast_p) {
			this.endingIndex++;
			this.fast_p = this.fast_p.next;
		}
		this.endingIndex--;
	}
	
	private void findStartOfLoop() {
		this.slow_p = this.head;
		this.startingIndex = 0;
		while (this.slow_p != this.fast_p) {
			this.startingIndex++;
			this.slow_p = this.slow_p.next;
			this.fast_p = this.fast_p.next;
		}
	}
}
