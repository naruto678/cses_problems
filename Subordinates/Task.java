import java.io.*; 
import java.util.stream.*;
import java.util.*; 

public class Task{ 
  public static void main(String args[]) throws Exception{
    BufferedReader br=new BufferedReader(new InputStreamReader(System.in)); 
    int n=Integer.parseInt(br.readLine());
    Integer arr[]=Arrays.stream(br.readLine().split("\\s+"))
                        .map(Integer::parseInt).toArray(Integer[]::new); 
    Graph graph=new Graph(n, arr); 
    int counter[]=graph.getCount(); 
    System.out.println(Arrays.toString(counter)); 
  }

  static class Graph{
    int n; 
    private ArrayList<Integer>[] adj; 
    private int counter[]; 
    private boolean marked[]; 
    Graph(int n, Integer arr[]){
      this.n=n ; 
      this.marked=new boolean[n+3]; 
      this.adj=new ArrayList[n+3] ;
      this.counter=new int[n+3]; 
      for(int i =0;i<this.adj.length ; i++)
        this.adj[i]=new ArrayList<Integer>(); 
      for(int i=0, j=2; i <arr.length;i++, j++){
        this.adj[arr[i]].add(j); 
        this.adj[j].add(arr[i]); 
      }
      this.dfs(1, 0 ); 
    }
    
    private void dfs(int source, int parent){
      counter[source]=1; 
      marked[source]=true; 
      for(int v: adj[source]){
        if(v!=parent){
          dfs(v, source); 
          counter[source]+=counter[v]; 
        }
      }
    }
    public int[] getCount(){
      return this.counter; 
    }

  }

}
