/*
    A program to demonstrate constant variable
*/
class Constants {
    public static void main(String[] args) {
        //Constasnt Score Values
        final int TOUCHDOWN = 6;
        final int CONVERSION = 1;
        final int FIELDGOAL = 3;

        //Calculate points scored
        int td, pat, fg, total;
        td = 4 * TOUCHDOWN;             //4X6=24
        pat = 3 * CONVERSION;           //3x1=3
        fg = 2 *FIELDGOAL;              //2x3=6
        total = (td + pat + fg);        //24+3+6=33
        //TOUCHDOWN = total * fg;          //statement to see error message for trying to change a constant when being compiled

        //Output calculated total
        System.out.println("Score: " + total);

    }
}
