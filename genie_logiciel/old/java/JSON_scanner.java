
//Parse the json file and put each pair of key/url of DTOs in an hashmap

HashMap<String, String> dto = new HashMap<String, String>(); 
						
Scanner scanner = new Scanner(json);
scanner.useDelimiter(",");
while(scanner.hasNext()) {
	String nextToken = scanner.next();
	Scanner scannerToken = new Scanner(nextToken);
	scannerToken.useDelimiter(":");
	String[] tokens = new String[3];			    
	int i = 0;
	while (scannerToken.hasNext()) {
		tokens[i] = scannerToken.next();
		i += 1;
	}
			    
	dto.put(tokens[0],tokens[1]+":"+tokens[2]);
			    	    
	scannerToken.close();		    
			    
}

scanner.close();
