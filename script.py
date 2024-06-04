def Reverse(lst):
   new_lst = lst[::-1]
   return new_lst
calc = open("calc.json", "w")
calc.write('{\n')
num = 0
for trainer_index in range(len(data.trainers.stats)):
  if num > 0:
    index_num = 1
    if num < 10:
        calc.write('\t"' + data.trainers.stats[trainer_index].name.title() + '_00' + str(num) + '":{\n')
    elif num < 100:
        calc.write('\t"' + data.trainers.stats[trainer_index].name.title() + '_0' + str(num) + '":{\n')
    else:
        calc.write('\t"' + data.trainers.stats[trainer_index].name.title() + '_' + str(num) + '":{\n')
    for mon_info in data.trainers.stats[trainer_index].pokemon:
      calc.write('\t\t"' + mon_info.mon.title() + '_' + str(index_num) + '":{\n\t\t\t"ability":"' + data.pokemon.stats[mon_info.mon].ability1.title() + '",\n\t\t\t')
      try:
        calc.write('"item":"' + mon_info.item.title() + '",')
      except:
        pass
      scaledIV = str(round(mon_info.ivSpread * .12156))
      calc.write('"nature":"Serious",\n\t\t\t"ivs":{"hp":' + scaledIV + ', "at":' + scaledIV + ', "df":' + scaledIV + ', "sa":' + scaledIV + ', "sd":' + scaledIV + ', "sp":' + scaledIV + '}')
      try:
        calc.write(',\n\t\t\t"moves":["' + mon_info.move1.title() + '","' + mon_info.move2.title() + '","' + mon_info.move3.title() + '","' + mon_info.move4.title() + '"]')
      except:
        calc.write(',\n\t\t\t"moves":["')
        count = 0
        for movesFromLevel in Reverse(list(data.pokemon.moves.levelup[mon_info.mon].movesFromLevel)):
          level = mon_info.level
          while level > 0 and count < 3:
            if movesFromLevel.pair.level == level:
              calc.write(data.pokemon.moves.names[movesFromLevel.pair.move].name.title() + '","')
              count = count + 1
            level = level - 1
          while level > 0 and count == 3:
            if movesFromLevel.pair.level == level:
              calc.write(data.pokemon.moves.names[movesFromLevel.pair.move].name.title() + '"]')
              count = count + 1
            level = level - 1
        if count < 3:
          calc.write('(No Move)","')
          count = count + 1
        if count == 3:
          calc.write('(No Move)"]')
          count = count + 1
      calc.write(',\n\t\t\t"level":' + str(mon_info.level) + '\n\t\t},\n')
      index_num = index_num + 1
    calc.write('\t},\n')
  num = num + 1
calc.write('}')
calc.close()