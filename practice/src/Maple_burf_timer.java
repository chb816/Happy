import java.util.Scanner;

abstract class User_info {
    protected int buff_time_influ;
    public User_info(int buff_time_influ){
        this.buff_time_influ = buff_time_influ;
    }

    abstract public int buff_calc();
}

class skil_info extends User_info{
    protected int skil_time;
    
    public skil_info(int buff_time_influ, int skil_time){
        super(buff_time_influ);
        this.skil_time = skil_time;
    } 

    public int buff_calc(){
        return ((super.buff_time_influ * this.skil_time) / 100)+ this.skil_time ;
    }
}
class ssle_skil {
    String ssle_name;
    
    int ssle_time;
    
    public ssle_skil(String name, int lv){
        this.ssle_name = name;
    }
    
    public void ssle_time(String ssle_name){
        System.out.print(this.ssle_name);
    }
}
// 
public class Maple_burf_timer {
    //testver
    public static void main(final String[] args){
        
        Scanner scanner = new Scanner(System.in);
        int buff_influ = scanner.nextInt();
        int time = scanner.nextInt();

        skil_info defalt_Skil_info = new skil_info(buff_influ, time);
        System.out.print(defalt_Skil_info.buff_calc());


        scanner.close();
    }
    
}