import java.util.*;
import java.io.*;
 
class Sol{
  public int mspf[]=new int[10001];
  public void erastho(int n){
 int i=0;
 for(i=2;i<10001;i++){
mspf[i]=i;
 }
 for(i=4;i<10001;i=i+2){
mspf[i]=2;
 }
 for(i=3;i*i<10001;i++){
if (mspf[i]==i){
  for (int j=i*i;j<10001;j=j+i){
mspf[j]=i;
  }
}

 }

 }
}
public class Main{

public static void main(String[] args) {
  // write your code here  
  int i;
  BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
  try{
    int n=Integer.parseInt(br.readLine());
    Sol s=new Sol();
    s.erastho(n);
    ArrayList<Integer> ar=new ArrayList<Integer>();
    while(n!=1){
      ar.add(s.mspf[n]);
      //System.out.print(s.mspf[n]+" ");
      n=n/s.mspf[n];
    }
    for( i=ar.size()-1;i>=0;i--){
      System.out.print(ar.get(i)+" ");
    }

  }
  catch(Exception e){
    System.out.println(e);
  }
 }
 
}
