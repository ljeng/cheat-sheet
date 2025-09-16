import java.util.*;

class FibonacciHeap<T> {
  private Node<T> min;
  private int n;
  
  public static class Node<T> {
    T data;
    int key;
    Node<T> parent;
    Node<T> child;
    Node<T> left;
    Node<T> right;
    int degree;
    boolean mark;
    
    Node(T data, int key) {
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
  
  public boolean isEmpty() {
  }
  
  public Node<T> insert(T data, int key) {
  }
  
  public Node<T> extractMin() {
  }
  
  public void decreaseKey(Node<T> x, int k) {
  }
  
  private void addToRootList(Node<T> node) {
  }
  
  private void removeFromRootList(Node<T> node) {
  }
  
  private void consolidate() {
  }
  
  private void link(Node<T> y, Node<T> x) {
  }
  
  private void cut(Node<T> x, Node<T> y) {
  }
  
  private void cascadingCut(Node<T> y) {
  }
}
