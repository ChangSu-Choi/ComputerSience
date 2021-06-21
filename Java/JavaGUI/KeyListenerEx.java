import javax.swing.*;
import java.awt.event.*;
import java.awt.*;


public class KeyListenerEx extends JFrame {
	private JLabel [] keyMessage;	//3개의 메세지를 출력할 레이블 컴포넌트 배열
	
	public KeyListenerEx() {
		setTitle("keyListener 예제");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		Container c = getContentPane();
		c.setLayout(new FlowLayout());
		c.addKeyListener(new MyKeyListener());
		
		//레이블 배열을 3개 생성하고 각 레이블 컴포넌트 생성
		keyMessage = new JLabel[3];	//레이블 배열 생성
		keyMessage[0] = new JLabel(" getKeyCode() ");
		keyMessage[1] = new JLabel(" getKeyChar() ");
		keyMessage[2] = new JLabel(" getKeyText() ");
		
		//3개의 레이블 컴포넌트를 컨텐트팬에 부착
		for(int i=0; i<keyMessage.length; i++) {
			c.add(keyMessage[i]);
			keyMessage[i].setOpaque(true);				//배경색이 보이도록 불투명 속성 설정
			keyMessage[i].setBackground(Color.YELLOW);	//배경색을 CYAN색으로 변경
		}
		
		setSize(300, 150);
		setVisible(true);
		
		//컨텐트팬이 키 입력을 받을 수 있도록 포커스 강제 지정
		c.setFocusable(true);
		c.requestFocus();
	}
	
	class MyKeyListener extends KeyAdapter{
		public void keyPressed(KeyEvent e) {
			int keyCode = e.getKeyCode();	//키 코드 알아내기
			char keyChar = e.getKeyChar();	//키 문자값 알아내기
			keyMessage[0].setText(Integer.toString(keyCode));
			keyMessage[1].setText(Character.toString(keyChar));
			keyMessage[2].setText(KeyEvent.getKeyText(keyCode));
			
			System.out.println("KeyPressed");	//콘솔창에 메소드 이름 출력
		}
		
		public void keyReleased(KeyEvent e) {
			System.out.println("KeyReleased");	//콘솔창에 메소드 이름 출력
		}
		
		public void keyTyped(KeyEvent e) {
			System.out.println("KeyTyped");		//콘솔창에 메소드 이름 출력
		}
	}
	
	public static void main(String[] args) {
		new KeyListenerEx();
	}
}
