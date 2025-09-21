import java.util.*;

class FibonacciHeap<E> {
  private Node<E> min;
  private int n;
  
  public static class Node<E> {
    T data;
    int key;
    Node<E> parent;
    Node<E> child;
    Node<E> left;
    Node<E> right;
    int degree;
    boolean mark;
    
    Node(E data, int key) {
      this.data = data;
      this.key = key;
      this.left = this;
      this.right = this;
    }
  }
  
  public FibonacciHeap() {
    min = null;
    n = 0;
  }
  
  public boolean empty() {
    return min == null;
  }
  
  public Node<E> insert(E data, int key) {
    Node<T> node = new Node<>(data, key);
    if (min == null) min = node;
    else {
      add(node);
      if (node.key < min.key) min = node;
    }
    n++;
    return node;
  }
  
  public Node<E> extractMin() {
    Node<E> current = min;
    if (current != null) {
      if (current.child != null) {
        Node<E> child = z.child;
        while (child != current.child) {
          Node<E> next = child.right;
          add(child);
          child.parent = null;
          child = next;
        }
      }
      remove(current);
      if (current == current.right) min = null;
      else {
        min = current.right;
        consolidate();
      }
      n--;
    }
    return currents;
  }
  
  public void decreaseKey(Node<E> x, int k) {
  }
  
  private void add(Node<E> node) {
    node.left = min;
    node.right = min.right;
    min.right.left = node;
    min.right = node;
  }
  
  private void remove(Node<E> node) {
    node.left.right = node.right;
    node.right.left = node.left;
  }
  
  private void consolidate() {
  }
  
  private void cut(Node<E> x, Node<E> y) {
  }
  
  private void cascadingCut(Node<E> y) {
  }
}
