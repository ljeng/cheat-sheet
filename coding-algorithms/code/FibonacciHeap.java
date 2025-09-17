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
  }
  
  public Node<E> extractMin() {
  }
  
  public void decreaseKey(Node<E> x, int k) {
  }
  
  private void add(Node<E> node) {
  }
  
  private void remove(Node<E> node) {
  }
  
  private void consolidate() {
  }
  
  private void cut(Node<E> x, Node<E> y) {
  }
  
  private void cascadingCut(Node<E> y) {
  }
}
