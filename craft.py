import pygame, CraftTable
from AssetsSystem import AssetsSystem

pygame.init()
width, height = 800, 600
WINDOWS = pygame.display.set_mode((width, height))
pygame.display.set_caption("Craft")
running = True
dragging = False
pos = (0, 0)

ct = CraftTable.CraftTable(WINDOWS)
ass_sys = AssetsSystem()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                ass_sys.buttons_clicked(pos)
                dragging = True

        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            ct.check_schemas(ass_sys)
            
        if event.type == pygame.MOUSEMOTION and dragging:
            pos = pygame.mouse.get_pos()
            ass_sys.items_move(pos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                pos = pygame.mouse.get_pos()
                ass_sys.delete_item(pos)

    WINDOWS.fill((0, 0, 0))

    ct.draw()
    ass_sys.draw(WINDOWS)

    pygame.display.update()
    
pygame.quit()