class Solution {
    public boolean isPalindrome(int x) {
        int numeroReverso = 0;
        int numeroOriginal = x;
        while (x > 0) {
            int digito = x % 10;
            numeroReverso = (numeroReverso * 10) + digito;
            x = x / 10;
        }

        if (numeroOriginal == numeroReverso) {
            return true;
        } else {
            return false;
        }
    }
    }
