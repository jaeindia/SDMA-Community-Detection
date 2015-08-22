import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.HashMap;

public class Main {

	public static void main(String[] args) throws IOException {
		String csvPath = "file\\graph1.csv";
		BufferedReader br = new BufferedReader(new FileReader(csvPath));
		HashMap<String, String> graph = new HashMap<String, String>();

		String line = null;
		String index[] = null;
		int lineNo = 0;

//		Read CSV file and store it in a hash map DS
		while ((line = br.readLine()) != null) {

//			**Test**
//			System.out.format("line No - %d - %s\n", lineNo, line);
			
			if (lineNo == 0) {
				index = line.split(",");
				index = Arrays.stream(index)
						.filter(s -> (s != null && s.length() > 0))
						.toArray(String[]::new);
				++lineNo;
				continue;
			}
			
			String tempString[] = line.split(",");

//			**Test**
//			System.out.format("tempString - %d - %s\n", lineNo, line);
//			System.out.format("0 - %s\n", index[0]);
			
			for (int i = 0; i < (tempString.length - 1); i++) {
				String key = index[i] + "-" + tempString[0];
				graph.put(key, tempString[i+1]);
			}
			
			++lineNo;
		}
		
		br.close();
		
//		Construnct the GML file
		
		
	}
}
