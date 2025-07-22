#nullable disable

partial class Program {
    public static void Main() {
        StreamReader reader = new StreamReader(Console.OpenStandardInput());
        StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());

        int[] NK = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
        int N = NK[0], K = NK[1];
        int[] A = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);

        merge_sort(A, 0, N - 1);
        if (K > 0) writer.WriteLine(-1);

        void merge_sort(int[] A, int left, int right)
        {
            if (left >= right) return;
            int mid = (left + right) / 2;
            merge_sort(A, left, mid);
            merge_sort(A, mid + 1, right);
            merge(A, left, mid, right);
        }

        void merge(int[] A, int left, int mid, int right)
        {
            int[] temp = new int[right - left + 1];
            int i = left, j = mid + 1, k = 0;
            while (i <= mid && j <= right)
            {
                if (A[i] < A[j])
                {
                    temp[k++] = A[i++];
                }
                else
                {
                    temp[k++] = A[j++];
                }
            }

            // 왼쪽 남은거
            while (i <= mid)
            {
                temp[k++] = A[i++];
            }
            // 오른쪽 남은거
            while (j <= right)
            {
                temp[k++] = A[j++];
            }
            // temp를 A에 다시 넣기(저장 발생)
            for (int l = 0; l < temp.Length; l++)
            {
                if (--K == 0)
                {
                    writer.WriteLine(temp[l]);
                }
                A[left + l] = temp[l];
            }
        }

        writer.Flush();
    }
}