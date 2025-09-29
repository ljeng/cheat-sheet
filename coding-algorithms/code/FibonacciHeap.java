import java.util.*;

class FibonacciHeap<E> {
  private Node<E> min;
  private int n;
  
  public static class Node<E> {
    E data;
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
        Node<E>[] nodes = new Node[(int) Math.floor(Math.log(n)
          / Math.log(2))];
        List<Node<E>> roots = new ArrayList<>();
        Node<E> current = min;
        while (current != min) {
          roots.add(current);
          current = current.right;
        }
        for (Node<E> root : roots) {
          Node<E> x = root;
          int degree = x.degree;
          while (nodes[degree] != null) {
            Node<E> y = nodes[degree];
            if (x.key > y.key) {
              Node<E> temp = x;
              x = y;
              y = temp;
            }
            link(y, x);
            nodes[d++] = null;
          }
          nodes[d] = x;
        }
        min = null;
        for (Node<E> node : nodes) if (node != null) {
          if (min != null) {
            add(node);
            if (node.key < min.key) min = node;
          }
          else min = node.left = node.right = node;
        }
      }
      n--;
    }
    return currents;
  }

  private void link(Node<E> x, Node<E> y) {
    remove(x);
    x.left = x.right = x;
    if (y.child != null) {
      x.left = y.child, x.right = y.child.right;
      y.child.right = y.child.right.left = x;
    }
    else y.child = x;
    x.parent = y;
    y.degree++;
    x.mark = false;
  }
  
  public void decreaseKey(Node<E> x, int k) {
    x.key = k;
    Node<E> y = x.parent;
    if (y != null && x.key < y.key) {
      cut(x, y);
      cascadingCut(y);
    }
    if (x.key < min.key) min = x;
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
  
  private void cascadingCut(Node<E> x) {
    Node<E> current = x;
    while (current != null) {
      Node<E> y = current.parent;
      if (y == null) break;
      if (current.mark) {
        if (current != current.right) {
          current.left.right = current.right;
          current.right.left = current.left;
          if (y.child == current) y.child = current.right;
        } else y.child = null;
        y.degree--;
        add(current);
        current.parent = null;
        current.mark = false;
        current = y;
      } else {
        current.mark = true;
        break;
      }
    }
  }
}
