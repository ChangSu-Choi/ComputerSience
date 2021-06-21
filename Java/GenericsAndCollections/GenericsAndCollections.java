/*********************************************************************************

 * 

 * 학과, 학번, 이름으로 식별되는 학생 n명(최소 10명 이상)의 자바 평가 점수에 대하여 평점 그리고 순위를 구하고,

 * 평균 미만인 학생에 대하여 재수강 여부를 선별하는 프로그램을 작성하려 한다. 다음 조건을 만족하도록 프로그래밍 하라.

 * 

 *   가. 학생의 신상 관련 정보를 Sinsang, 자바 점수 관련 정보를 JavaScore 라는 클래스로 정의할 것

 *       - 학생 신상 관련 정보 : 컴공, 20201007, 방탄소년

 *       - 자바 점수 관련 정보 : 점수, 평점, 순위, 재수강여부  단, 재수강 여부는 점수가 평균 미만인 학생에 대하여 boolean값 

 *      true로 처리하며 이를 위한 변수를 private boolean retake로 선언할 것

 *      

 *   나. n명의 신상 및 점수를 관리하기 위해 신상은 Vector를, 점수는 ArrayList를 이용하며 

 *      이들을 '키'와 '값'으로  관리하기 위해 HashMap를 사용할 것. 

 *      단, 해쉬맵의 매개변수는 Vector와 ArrayList의 요소로 지정할 것. 

 *      

 *   다. 신상정보(학과, 학번, 이름)는 초기화를 통해 Vector를 완성하고 점수는 커 입력한 후, 신상정보와 해당 점수를 출력할 것. 

 *      단, 점수 입력 시 InputMismatch 예외를 처리하고 재수강 학생이 존재하도록 적절히 점수를 분포하여 입력할 것.

 *      

 *   라. 평균을 위한 변수는 static double average으로 선언하고, 메소드 GetAverage에서 평균을 구하되

 *      Iterator 인터페이스를 사용할 것

 *      

 *   마. 메소드 SetRanking에서 순위(등수)를 결정하고 순위를 JavaScore에 저장할 것

 *   

 *   바. '키'로 Sinsang의 학생 이름을, '값'으로 JavaScore의 점수를 사용하는 해쉬맵을 이용하여 학생의 이름으로 점수를 검색
 	 함. 단, 검색은 1회에 한함.   

 *   

 *   사. 상기 해쉬맵을 이용하여 입력한 학생 정보(신상 및 점수관련 정보)를 아래와 같이 출력할 것

 *   	[1] 학과1 학번 이름 점수(순위) 평점 재수강-미대상

 *   			. . .

 *   	[10] 학과5 학번 이름 점수(순위) 평점 재수강-대상

 *   

 *      그리고 별표 막대 그래프를 아래와 같이  출력할 것.



 *  A(3명) | *** 

 *  B(3명) | ***

 *  C(2명) | **

 *  D(1명) | *

 *  F(1명) | *

 *  ------------------------

 *  총합 10명(평균 79점)

 *  

 ***********************************************************************/
import java.util.Scanner;
import java.util.InputMismatchException;
import java.util.Vector;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
//학생의 신상 관련 정보 클래스
class Sinsang{
	String major, name;
	int code;
	
	Sinsang(String major, int code, String name){
		this.major = major;
		this.code = code;
		this.name = name;
	}
	
}
//자바 점수 관련 정보 클래스
class JavaScore{
	double score;
	int int_rank = 0;
	char char_rank = 'F';
	private boolean retake = false;
	
	JavaScore(double score){
		this.score = score;
	}
	
	public void SetRetakeToTrue(){
		retake = true;
	}
	
	public boolean GetRetake() {
		return retake;
	}
}

public class GenericsAndCollections {
	static double average = 0;

	public static void main(String[] args) {
		//A,B,C,D,E,F등급 인원 카운트 배열 선언
		int[] count_char_rank;
		count_char_rank = new int[5];
		//n명의 학생 수 선언
		Scanner sc = new Scanner(System.in);
		System.out.print("학생 몇 명이신가요?(초기화가 10명이니 10명만 되게 구현했습니다): ");
		final int n = sc.nextInt();

		//n명의 신상 vector 및 점수 ArrayList를 생성
		Vector<Sinsang> v = new Vector<Sinsang>(n);
		ArrayList<JavaScore> a = new ArrayList<JavaScore>(n);
		HashMap<String, JavaScore> student_map = new HashMap<String, JavaScore>();
		
		InputStudData(v, a, student_map);  // 학과, 학번, 이름, 성적 입력

		

		InputReport(v, a); 	// 데이터 입력 후 입력된 결과 확인용

		
		
		GetAverage(a); 		// 평균을 구하여 static 변수 average에 저장함
		
	

		GetGrade(a, count_char_rank);			// 평점(학점) 구하기, 여기서 재수강 여부도 판정함

			
		
		SetRanking(a);			//  평점을 근거로 순위(rank)를 결정

		
		
		SearchScore(student_map); 	// 해쉬맵을 이용하여 학생의 이름으로 점수를 검색함

		
		
		OutputReport(v, student_map); 	// 해쉬맵을 이용하여 신상정 보와 성적 관련 정보를 모두 출력 


		
		GradeBunpo(count_char_rank);			// 학점 분포 막대 그래프 그리기
		
		sc.close();
	}
	
	//데이터를 Vector, ArrayList에 입력후 HashMap에 삽입한다
	static void InputStudData(Vector<Sinsang> v_sinsang, ArrayList<JavaScore> a_javascore, HashMap<String, JavaScore> map) {
		//데이터 입력
		v_sinsang.add(new Sinsang("컴공", 20201001, "초롱이"));
		v_sinsang.add(new Sinsang("전자", 20192011, "댕댕이"));
		v_sinsang.add(new Sinsang("컴공", 20178001, "아롱이"));
		v_sinsang.add(new Sinsang("컴공", 20181001, "따롱이"));
		v_sinsang.add(new Sinsang("화공", 20201801, "냥냥이"));
		v_sinsang.add(new Sinsang("컴공", 20211001, "이순신"));
		v_sinsang.add(new Sinsang("컴공", 20182031, "강감찬"));
		v_sinsang.add(new Sinsang("전자", 20218001, "을지문덕"));
		v_sinsang.add(new Sinsang("화공", 20181001, "김유신"));
		v_sinsang.add(new Sinsang("전자", 20201811, "계백"));
		
		//score = {92, 86, 47, 75, 83, 69, 88, 96, 77, 90};
		Scanner sc = new Scanner(System.in);
		try {
			for(int i = 0; i < v_sinsang.size(); i++) {
				System.out.print(v_sinsang.get(i).name+"의 점수를 입력하세요 : ");
				a_javascore.add(new JavaScore(sc.nextDouble()));
				//HashMap에 Key와 Value 삽입
				map.put(v_sinsang.get(i).name, a_javascore.get(i));
			}
		}
		catch(InputMismatchException e) {
			System.out.println("입력값을 다시 확인해 주세요.");
			System.exit(1);
		}
		sc.close();
		System.out.println();
	}
	
	// 데이터 입력 후 입력된 결과를 확인한다
	static void InputReport(Vector<Sinsang> v_sinsang, ArrayList<JavaScore> a_javascore){
		for(int i = 0; i < v_sinsang.capacity(); i++) {
			System.out.println("["+(i+1)+"] "+v_sinsang.get(i).major+" "+v_sinsang.get(i).code+" "
		+v_sinsang.get(i).name+" "+(int)a_javascore.get(i).score);
		}
		System.out.println();
	}
	
	// 평균을 구하여 static 변수 average에 저장함
	static void GetAverage(ArrayList<JavaScore> a_javascore){
		//Iterator 인터페이스를 사용할 것
		Iterator<JavaScore> it = a_javascore.iterator();
		while(it.hasNext()) {
			average += it.next().score;
		}
		average /= a_javascore.size();
	}
	
	// 평점(학점) 구하기, 여기서 재수강 여부도 판정함
	static void GetGrade(ArrayList<JavaScore> a_javascore, int [] count_char_rank) {
		//각 등급의 커트라인을 조정
		int over_A = 90, over_B = 80, over_C = 70, over_D = 60;
		
		//등급당 인원 카운트
		for(int i = 0; i < a_javascore.size(); i++) {
					if(a_javascore.get(i).score >= over_A) {a_javascore.get(i).char_rank = 'A'; count_char_rank[0]++;}
					else if(a_javascore.get(i).score >= over_B) {a_javascore.get(i).char_rank = 'B'; count_char_rank[1]++;}
					else if(a_javascore.get(i).score >= over_C) {a_javascore.get(i).char_rank = 'C'; count_char_rank[2]++;}
					else if(a_javascore.get(i).score >= over_D) {a_javascore.get(i).char_rank = 'D'; count_char_rank[3]++;}
					else {a_javascore.get(i).char_rank = 'F'; count_char_rank[4]++;}
					}
		
		
		//재수강 여부 판정
		for(int i =0; i < a_javascore.size(); i++)
			if(a_javascore.get(i).score < average)
				a_javascore.get(i).SetRetakeToTrue();
	}
	
	//평점을 근거로 순위(rank)를 결정
	static void SetRanking(ArrayList<JavaScore> a_javascore) {
		double[] copy_score_list = new double[a_javascore.size()];
		
		for(int i = 0; i < a_javascore.size(); i++)
			copy_score_list[i] = a_javascore.get(i).score;
		
		//copy_score_list를 내림차순으로 소트
		double temp = 0;
		for(int i=0 ; i<copy_score_list.length-1; i++) {
		      for (int j = i+1; j < copy_score_list.length; j++) {
		        //앞의 수가 더 크다면 swap
		        if(copy_score_list[i] < copy_score_list[j]) {
		          temp = copy_score_list[i];
		          copy_score_list[i] = copy_score_list[j];
		          copy_score_list [j] = temp;
		        }
		      }
		    }
		
		//sort된 리스트와 원본의 순위를 비교후 순위 결정
		for(int i= 0; i < a_javascore.size(); i++)
			for(int j = 0; j < copy_score_list.length; j++) {
				if(a_javascore.get(i).score == copy_score_list[j])
					a_javascore.get(i).int_rank = j+1;
			}
	}
	
	// 해쉬맵을 이용하여 학생의 이름으로 점수를 검색함
	static void SearchScore(HashMap<String, JavaScore> map) {
		Scanner sc = new Scanner(System.in);
		while(true) {
			System.out.print("검색할 학생의 이름을 입력하세요 : ");
			String name = sc.nextLine();
			
			JavaScore java_score = map.get(name);
			
			if(java_score == null) {
				System.out.println(name+"은 존재하지 않습니다.");
				break;
			}
			else {
				System.out.println("이름 : "+name+", 점수 : "+java_score.score+"\n");
				break;
				}
			}
		
		sc.close();
		}
	
	// 해쉬맵을 이용하여 신상 정보와 성적 관련 정보를 모두 출력 
	static void OutputReport(Vector<Sinsang> v_sinsang, HashMap<String, JavaScore> map) {
		Iterator<Sinsang> it = v_sinsang.iterator();
		int i = 1;
		while(it.hasNext()) {
			//Sinsang에 관한 정보 불러오기
			Sinsang sin = it.next();
			String major = sin.major, name = sin.name;
			int code = sin.code;
			
			//해시맵을 통해 JavaScore객체 불러오기
			JavaScore java_score = map.get(name);
			int score = (int)java_score.score;
			int int_rank = java_score.int_rank;
			char char_rank = java_score.char_rank;
			boolean retake = java_score.GetRetake();
			String sugang;
			if(retake) sugang = "대상자";
			else sugang = "미대상자";
			System.out.println("["+i+"] "+major+" "+code+" "+name+" "+score+"("+int_rank+") "+char_rank+" 재수강 -"+sugang);
			i++;
		}
	}
	
	// 학점 분포 막대 그래프 그리기
	static void GradeBunpo(int[] count) {
		//등급 마다 몇명인지 별을 이용하여 출력
		System.out.print("\nA("+count[0]+"명)  | ");
		for(int j = 0; j < count[0]; j++) System.out.print("*");
		System.out.print("\nB("+count[1]+"명)  | ");
		for(int j = 0; j < count[1]; j++) System.out.print("*");
		System.out.print("\nC("+count[2]+"명)  | ");
		for(int j = 0; j < count[2]; j++) System.out.print("*");
		System.out.print("\nD("+count[3]+"명)  | ");
		for(int j = 0; j < count[3]; j++) System.out.print("*");
		System.out.print("\nF("+count[4]+"명)  | ");
		for(int j = 0; j < count[4]; j++) System.out.print("*");
		
		int total = 0;
		for(int i = 0; i< count.length; i++)
			total += count[i];
		
		System.out.print("\n----------------------------------\n");
		System.out.print("총합 "+total+"명(평균 "+average+"점)");
	}
		
}
