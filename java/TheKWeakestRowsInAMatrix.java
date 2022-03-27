import java.util.Arrays;

public class TheKWeakestRowsInAMatrix {
	public static int[] kWeakestRows(int[][] mat, int k) {
		int n = mat[0].length;
		for (int i = 0; i < mat.length; i++) {
			int count = 0;
			for (int j = 0; j < n; j++) {
				if (mat[i][j] == 1)
					count++;
			}
			mat[i][n - 1] = i;
			mat[i][0] = count;
		}
		Arrays.sort(mat, (a, b) -> Integer.compare(a[0], b[0]));
		int[] ans = new int[k];
		for (int i = 0; i < k; i++) {
			ans[i] = mat[i][n - 1];
		}
		return ans;
	}

	public static void main(String[] args) {

		// int[][] mat = { { 1, 1, 0, 0, 0 }, { 1, 1, 1, 1, 0 }, { 1, 0, 0, 0, 0
		// }, { 1, 1, 0, 0, 0 }, { 1, 1, 1, 1, 1 } };
		// int k = 3;
		int[][] mat = { { 1, 0, 0, 0 }, { 1, 1, 1, 1 }, { 1, 0, 0, 0 }, { 1, 0, 0, 0 } };
		int k = 2;

		System.out.println(Arrays.toString(kWeakestRows(mat, k)));

	}

}
