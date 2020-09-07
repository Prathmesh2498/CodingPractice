package Graph;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.Stack;

class Graph {

	private int v;
	private LinkedList<Integer> adj[];

	@SuppressWarnings("unchecked")
	Graph(int v) {
		this.v = v;
		adj = new LinkedList[this.v];
		for (int i = 0; i < v; i++) {
			adj[i] = new LinkedList();
		}

	}

	@Override
	public String toString() {
		// TODO Auto-generated method stub
		for (int i = 0; i < v; i++) {
			Iterator<Integer> itr = adj[i].listIterator();
			while (itr.hasNext()) {
				int n = itr.next();
				System.out.println(i + " " + n);
			}
		}
		return super.toString();
	}

	// Functions of class Graph
	void addEdge(int u, int v) {
		adj[u].add(v);
	}

	void bfs(int source) {
		int current;// Store values popped from queue
		int size = this.v;
		boolean[] visited = new boolean[size];

		for (int i = 0; i < size; i++) {
			visited[i] = false;
		}

		LinkedList<Integer> queue = new LinkedList<Integer>();
		visited[source] = true;
		queue.add(source);

		while (!queue.isEmpty()) {
			current = queue.poll();
			System.out.print(current + " ");

			Iterator<Integer> i = adj[current].listIterator();

			while (i.hasNext()) {
				int n = i.next();
				if (!visited[n]) {
					visited[n] = true;
					queue.add(n);
				}

			}

		}
	}
	
	void dfs(int source) {
		int current;
		boolean[] visited = new boolean[this.v];
		Stack<Integer> st = new Stack();
		
		st.add(source);
		visited[source] = true;
		while(!st.isEmpty()) {
			current = st.pop();
			System.out.print(current + " ");
			
			Iterator<Integer> it = adj[current].listIterator();
			
			while(it.hasNext()) {
				int n = it.next();
				if(!visited[n]) {
					visited[n] = true;
					st.add(n);
				}
			}
		}
	}
}

public class driver {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Graph g;
		g = new Graph(4);
		g.addEdge(0, 1);
		g.addEdge(0, 2);
		g.addEdge(1, 2);
		g.addEdge(2, 0);
		g.addEdge(2, 3);
		g.addEdge(3, 3);

		// System.out.println(g); Print Adjecency List
		System.out.println("BFS From 1");

		g.bfs(2);
		System.out.println(" ");
		g.dfs(1);
	}

}
