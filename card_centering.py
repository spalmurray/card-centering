import card_reader as cr

if __name__ == "__main__":
    path = input("Enter path to card image file "
                 "(relative to this Python file's location):")
    card = cr.Card(path)
    centering = card.get_centering()
    print(f'Centering is {centering[0]}:{centering[1]}.')
    options = input('Save centering output?(y/n): ')
    if options.lower() == 'y':
        card.save()
