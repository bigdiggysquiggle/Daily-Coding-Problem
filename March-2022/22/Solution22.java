import javax.xml.crypto.Data;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

class DataApi    {
    private List<Integer> records;
    public DataApi()    {
        this.records = new ArrayList<>();
    }
    public DataApi(List records)    {
        this.records = records;
    }
    public void record(Integer orderID) {
        records.add(orderID);
    }
    public Integer get_last(Integer i) {
        return records.get(records.size() - i - 1);
    }
}

public class Solution22 {
    public static void main(String[] args)  {
        Random rng = new Random(System.currentTimeMillis());
        DataApi api = new DataApi();
        for (int i = 0; i < 10; i++) {
            Integer rec = rng.nextInt();
            System.out.println("Creating record: " + rec);
            api.record(rec);
        }
        for (int i = 0; i < 10; i++) {
            System.out.println("Retrieving record " + i);
            System.out.println(api.get_last(i));
        }
    }
}