import javax.swing.*;

public class MenuEx extends JFrame{
	public MenuEx() {
		setTitle("Menu 만들기 예제");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		createMenu();	//메뉴 생성, 프레임에 삽입
		setSize(250, 200);
		setVisible(true);
		
	}
	
	private void createMenu() {
		JMenuBar mb = new JMenuBar();				//메뉴바 생성
		JMenu screenMenu = new JMenu("Screen:");	//Screen 메뉴 생성
		
		//Screen 메뉴에 메뉴아이템 생성 삽입
		screenMenu.add(new JMenuItem("Load"));
		screenMenu.add(new JMenuItem("Hide"));
		screenMenu.add(new JMenuItem("ReShow"));
		screenMenu.addSeparator();	//분리선 삽입
		screenMenu.add(new JMenuItem("Exid"));
		
		//메뉴바에 메뉴 삽입
		mb.add(screenMenu);	//screen 메뉴 삽입
		mb.add(new JMenu("Edit"));	//Edit 메뉴 생성 삽입
		mb.add(new JMenu("Edit"));	//Source 메뉴 생성 삽입
		mb.add(new JMenu("Edit"));	//Project 메뉴 생성 삽입
		mb.add(new JMenu("Edit"));	//Run 메뉴 생성 삽입
		
		
		//메뉴바를 프레임에 부착
		setJMenuBar(mb);
	}
	
	public static void main(String[] args) {
		new MenuEx();
	}
}
