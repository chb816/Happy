//like 팩맨
//gui 이용 제대로

abstract class GameObject{
    protected int distance;
    protected int x, y;

    public GameObject(int startX, int startY, int distance){ //생성자
        this.x = startX;
        this.y = startY;
        this.distance = distance;
    }
    public int getx(){ //일반 메소드
        return x;
    }
    public int gety(){
        return y;
    }
    public boolean collide(GameObject p){
        if(this.x == p.getx() && this.y == p.gety())
            return true;
        else
            return false;
    }
    protected abstract void move(); //추상메소드
    protected abstract char getShape();
    
}
class bear extends GameObject{
    public bear(int startX, int startY, int distance) {
        super(startX, startY, distance);
    }

    @Override
    protected void move() {

    }
    @Override
    protected char getShape() {

        return 'a';
    }
}

class fish extends GameObject{
    public fish(int startX, int startY, int distance) {
        super(startX, startY, distance);
    }
    @Override
    protected void move(){

    }
    @Override
    protected char getShape() {
        return 'a';
    }
}
//gameobject 상속받아 move getshape collide 구현

public class Congame_ex{
    public static void main(String[] args){

    }
}

