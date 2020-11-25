import java.util.Scanner;


class Player {
    String name;
    String word;
    char now_lastword;
    char now_fstword;
    int word_index;
    char yet_lastword;

    public Player(String name){
        this.name = name;
        

    }
    

    void get_word(String word){
        this.word = word;   
        word_index = word.length() -1;
        this.now_lastword = word.charAt(word_index);
        this.now_fstword = word.charAt(0);
        
        
    }
    void run(Player player){
        System.out.println(player.name+">>"+player.word);
        System.out.println(player.yet_lastword);
        player.get_word(player.word);
    
    }

    boolean check(char a, char b){
        if(a == b){
            return true;
        }
        else{
            System.out.println("ㅅㄱㅂㅇ");
            return false;
        }
    }
}

public class Wordgameapp {
    public static void main(String[] args) {
        int loop = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println("참가자 인원을 입력해 주세요");
        int player_cnt = sc.nextInt();
        Player [] players;
        players = new Player[player_cnt];
        for(int i = 0; i < players.length; i ++){
            System.out.println("참가자의 이름을 입력해 주세요");
            String name = sc.next();
            players[i] = new Player(name);
        }
        char startword = '지';
        System.out.println("시작단어 지");
        int cnt=0;
        while(loop == 0){
            for (int i = 0; i<players.length; i++) {
                players[i].word = sc.next();
                players[i].run(players[i]);
                cnt++;
                if ((i>=1)&&(players[i].check(players[i].now_fstword,players[i-1].now_lastword) == false)){
                    loop = 1;
                    break;
                }
                else if ((cnt<4)&&(i==0)&&(players[i].check(startword, players[i].now_fstword)==false)){
                    loop = 1;
                    break;
                }
                else if ((cnt>4)&&(i==0)&&(players[i].check(players[i].now_fstword,players[-1].now_lastword)==false)){
                    loop = 1;
                    break;
                }
            }
        }
        sc.close();
    }
}