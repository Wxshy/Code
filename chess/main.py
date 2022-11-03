import pygame
import os

class Piece:
    def __init__(self,name, colour, image):
        self.name = name
        self.colour = colour
        self.isKing = True if name == 'k' else False
        self.image = image
    def set_pos(self, rank, file):
        self.rank = rank
        self.file = file
    
    

def draw_board():
    board = pygame.Surface((800,800))
    board.fill((255,255,255))
    size = 100
    cnt = 0
    for i in range(0,8):
        for z in range(0,8):
            #check if current loop value is even
            if cnt % 2 == 0:
                pygame.draw.rect(board, (232, 235, 239),[size*z,size*i,size,size])
            else:
                pygame.draw.rect(board, (125, 135, 150), [size*z,size*i,size,size])
            cnt +=1
        #since theres an even number of squares go back one value
        cnt-=1
    
    pygame.draw.rect(board,(255, 215, 0),[0,0,8*size,8*size],2)


    return board

def get_pieces():
    pieces = []
    file_names = ['blk_b.png',	'blk_n.png',	'blk_q.png',	'wht_b.png',	'wht_n.png',	'wht_q.png',
'blk_k.png',	'blk_p.png',	'blk_r.png',	'wht_k.png',	'wht_p.png',	'wht_r.png']
    for name in file_names:
        image = pygame.image.load(os.path.join('pieces/', name))
        piece_colour = name[0]
        piece_name = name[4:name.index('.')]
        pieces.append(Piece(piece_name, piece_colour, image))
    return pieces

    
def starting_positions(pieces, board):

    starting_fen = "rnbqkbnr/pppppppp/////PPPPPPPP/RNBQKBNR"
    rank = 0
    file = 0

    for i in starting_fen:
        colour = 'b'
        if i.isupper():
            colour = 'w'
        if i == '/': 
            rank += 1
            file = 0
        else:
            for p in pieces:
                if getattr(p, 'name') == i.lower() and getattr(p, 'colour') == colour:
                    p.set_pos(rank, file)
                    print(p.__dict__)
                    board.blit(p.image, (file*100, rank*100))
        
            file += 1
        
    

    return board, pieces





def main():
    board = draw_board()
    pieces = get_pieces()

    board, pieces = starting_positions(pieces, board)
    
    def disp_update():
        window.blit(board, (2,2))
        pygame.display.update()

    pygame.init()
    window = pygame.display.set_mode((852,802))
    run = True
    #cells are 100x100
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print(mx,my)

                #code for finding piece in the square mx,my
                rank = int(str(mx)[0])
                file = int(str(my)[0])
                print("mouse: ", rank, file)

                for p in pieces:
                    if (p.rank == rank and p.file == file):
                        print(p.__dict__)
                    
                        #----------------------------------

        disp_update()


main()