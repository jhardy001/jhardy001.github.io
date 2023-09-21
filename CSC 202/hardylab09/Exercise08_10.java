package hardylab09;

public class Exercise08_10 {
	public static void main(String[] args) {
		int[][] mArray = new int[4][4];
 
		for (int i = 0; i < mArray.length; i++) {
			for (int j = 0; j < mArray[i].length; j++) {
				mArray[i][j] = (int)(Math.random() * 2);
			}
		}

		for (int i = 0; i < mArray.length; i++) {
			for (int j = 0; j < mArray[i].length; j++) {
				System.out.print(mArray[i][j]);
			}
			System.out.println();
		}

		System.out.println("The largest row index: " + biggestRow(mArray));
		System.out.println("The largest row column: " + biggestColumn(mArray));

	}

	public static int biggestRow(int[][] m) {
		int maxRowIndex = 0;
		int max = 0;
		for (int i = 0; i < m.length; i++) {
			int count = 0;
			for (int j = 0; j < m[i].length; j++) {
				if (m[i][j] == 1)
					count++;
			}
			if (count > max) {
				max = count;
				maxRowIndex = i;
			}
		}
		return maxRowIndex;
	}

	public static int biggestColumn(int[][] m) {
		int maxColumnIndex = 0;
		int max = 0;
		for (int col = 0; col < m[0].length; col++) {
			int count = 0;
			for (int row = 0; row < m.length; row++) {
				if (m[row][col] == 1)
					count++;
			}
			if (count > max) {
				max = count;
				maxColumnIndex = col;
			}
		}
		return maxColumnIndex;
	}
}