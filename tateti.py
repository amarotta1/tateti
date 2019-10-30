
class TaTeTi():

    def __init__(self,board=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']):
        
        self.board = board
        

    def full(self):

        for i in self.board:
            if i == " ":
                return False
        return True
        

        
    def win(self):

        #Filas 
        for i in range(0,7,3):
            if self.board[i] == self.board[i+1] == self.board[i+2] == "x":
                return True

        for i in range(0,7,3):
            if self.board[i] == self.board[i+1] == self.board[i+2] == "o":
                return True

        #Columnas
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] == "x":
                return True
        
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] == "o":
                return True


        #Diagonales

        if self.board[0] == self.board[4] == self.board[8] == "o":
            return True

        if self.board[0] == self.board[4] == self.board[8] == "x":
            return True

        if self.board[2] == self.board[4] == self.board[6] == "o":
            return True

        if self.board[2] == self.board[4] == self.board[6] == "x":
            return True





        return False


    def validate(self,position):
       
        if self.board[position-1] != " ":
            return False
        else:
            return True 
                            

        
    def assign(self,position,piece):

        if self.board[position-1] != " ":
            raise Exception
        else:
            self.board[position-1] = piece


    def draw_board(self):

        printer_board = self.board.copy()

        print (printer_board)

        for i in range(9):
            if printer_board[i] == " ":
                printer_board[i] = str(i+1)


        return "\n " + printer_board[0] + " | "+printer_board[1]+" | "+ printer_board[2] + " \n---+---+---\n "+ printer_board[3]+ " | "+ printer_board[4] + " | "+ printer_board[5]+" \n---+---+---\n " +printer_board[6] +" | "+ printer_board[7] +" | " +printer_board[8] +" \n"

    

        
