class all_champ{//ㄹㅇ 챔피언 정보만
    String champs [];//Riot api
}

class line {
    String lines [] = {"top","jg","mid","ad","sup"};
}

class user { //user info
    String line; //line class 참조
    String champ; //all_champ class 참조
    String name;
    //쳐던진거, 템판거, 승률, 챔폭 Riot api

    public user(String name){
        this.name = name;
        //api
    }

    public void idea(String name) {
        //미친승률 보유
        //티어, 큐 불일치
        
    }
    public void tlol(){
        //템판거
        //첨하는거
        //숙련도
    
    }
}


public class SSap_scanner {
    public static void main(String[] args){

    }
}