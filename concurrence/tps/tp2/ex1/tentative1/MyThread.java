import java.util.Random;
public class MyThread extends Thread{
	int myId;
	Lock lock;
	Random r= new Random();

	public MyThread(int id, Lock lock){
		myId= id;
		this.lock= lock;	
	}	

	void nonCriticalSection(){ 
		System.out.println(myId+"n'est pas en SC");
		mySleep(r.nextInt(1000));
	}
	
	public void run(){
		while(true){
			lock.requestCS(myId);
			//section critique
			lock.releaseCS(myId);
			//section non critique
		}
	}

	public void main(String[] args) throws Exception{
		MyThread[];
		int N= Integer.parseInt(args[0]);
		t= new myThread[n];
		Lock= lock new Attempt1();
		for(int i= 0; i<len; i++){
			t[i]= new MyThread(i,lock);
			t[i].start();
		}
	}
}
