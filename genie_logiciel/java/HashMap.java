package com.library.resources;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class BookData {
	
	
	//Key = Title, Value = Book
	private HashMap<String, Book> bookList = new HashMap<String, Book>();
	 
	
	public BookData() {
		super();
		initialiser();
	}

	public HashMap<String, Book> getBooks(){
		return bookList;		 
	}
	
	public Book getBook(String id){
		return bookList.get(id);		 
	}
	
	public  void initialiser(){
		
		List<String> publisherBooks =  new ArrayList<String>();
		publisherBooks.add("title1");
		publisherBooks.add("title2");
		publisherBooks.add("title3");
		
		List<Publisher> publishers = new ArrayList<Publisher>();
		List<Book> books = new ArrayList<Book>();
		
		
		for(int i = 1; i <= 50; i++) {
			
			publishers.add(new Publisher("name" + Integer.toString(i), "address" + Integer.toString(i),publisherBooks));
			books.add(new Book("title" + Integer.toString(i), "author" + Integer.toString(i), 953495758 + i, publishers.get(i-1)));
			
		}
				
		for(int i = 1; i <= 50; i++) {
			
			bookList.put("title" + Integer.toString(i), books.get(i-1));		
		}
		
	} 
	
}
