import time
from colorama import Fore, Back, Style

print("good mornig sir \nwelcome to our group project:\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tcreated by->harshit ayush ka papa Agrawal\n".title(),
      "\t\t\t\t\t\t\t\t\t<-sentimental analysis->".upper())
print("\t\t\t\t\t\t\t\t\t________________________")
time.sleep(5)
c = 0
print("\t\n<please remember to put an foolish stop(.) at end of the sentence>\n".title())
while (True):

    c += 1
    if (c == 1):
        sentence = input(
            Fore.YELLOW+"Enter your sentence here:".title()).lower()
        print(Style.RESET_ALL)
    else:
        sentence = input(
            Fore.YELLOW+"\n\nif you want to continue than\nenter you sentence below \nelse enter 'q' -> ".title()).lower()
        print(Style.RESET_ALL)
        if (sentence == "q"):
            print("thank you for using our code\n have a great day sir".title())
            break
    sentence = sentence.replace(".", " .")
    if (sentence.endswith == False):
        print("sorry but it looks like you forget to put foolish stop at the end.".title())
    elif (sentence.endswith(".")):
        print("ye sahi kaam kara apne")
    sen = sentence.split()
    n = p = 0

    for j in sen:
        if ('adaptable' == j or
           'adventurous' == j
            or
            'amazing' == j or
            'amiable' == j
            or
            'beautiful' == j
            or
            'becoming' == j
            or
            'beloved' == j
            or
            'blessed' == j
            or
            'blissful' == j
            or
            'brotherly' == j
            or
            'calming' == j
            or
            'captivating' == j
            or
            'charming' == j
            or
            'cherished' == j
            or
            'comforting' == j
            or
            'compelling' == j
            or
            'considerable' == j
            or
            'credible' == j
            or
            'dapper' == j
            or
            'darling' == j
            or
            'delicious' == j
            or
            'delightful' == j
            or
            'dependable' == j
            or
            'desirable' == j
            or
            'dreamy' == j
            or
            'durable' == j
            or
            'elegant' == j
            or
            'empowering' == j
            or
            'enchanting' == j
            or
            'endearing' == j
            or
            'energising' == j
            or
            'enjoyable' == j
            or
            'enlightening' == j
            or
            'exceptional' == j
            or
            'fabulous' == j
            or
            'fancy' == j
            or
            'fantastic' == j
            or
            'fashionable' == j
            or
            'faultless' == j
            or
            'fetching' == j
            or
            'flourishing' == j
            or
            'formidable' == j
            or
            'fulfilling' == j
            or
            'funny' == j
            or
            'generous' == j
            or
            'gifted' == j
            or
            'glamorous' == j
            or
            'gleaming' == j
            or
            'glowing' == j
            or
            'godly' == j
            or
            'gracious' == j
            or
            'pretty' == j or
            'gratifying' == j
            or
            'happening' == j
            or
            'harmonious' == j
            or
            'heavenly' == j
            or
            'honourable' == j
            or
            'ideal' == j
            or
            'important' == j
            or
            'incredible' == j
            or
            'indispensable' == j
            or
            'indisputable' == j
            or
            'influential' == j
            or
            'inspiring' == j
            or
            'interesting' == j
            or
            'irresistible' == j
            or
            'joyful' == j
            or
            'jolly' == j
            or
            'jovial' == j
            or
            'kindly' == j
            or
            'kingly' == j
            or
            'leading' == j
            or
            'legendary' == j
            or
            'liberating' == j
            or
            'likeable' == j
            or
            'lordly' == j
            or
            'lovable' == j
            or
            'luscious' == j
            or
            'luxurious' == j
            or
            'magical' == j
            or
            'majestic' == j
            or
            'memorable' == j
            or
            'mesmerizing' == j
            or
            'mighty' == j
            or
            'miraculous' == j
            or
            'motivational' == j
            or
            'nifty' == j
            or
            'obliging' == j
            or
            'optimal' == j
            or
            'original' == j
            or
            'out' == j
            or
            'of' == j
            or
            'this' == j
            or
            'world' == j
            or
            'outgoing' == j
            or
            'palatable' == j
            or
            'paramount' == j
            or
            'peaceful' == j
            or
            'peachy' == j
            or
            'perfect' == j
            or
            'phenomenal' == j
            or
            'picturesque' == j
            or
            'pleasant' == j
            or
            'pleasing' == j
            or
            'pleasurable' == j
            or
            'positive' == j
            or
            'powerful' == j
            or
            'praiseworthy' == j
            or
            'precious' == j
            or
            'prestigious' == j
            or
            'prizewinning' == j
            or
            'promising' == j
            or
            'quality' == j
            or
            'radiant' == j
            or
            'reasonable' == j
            or
            'refreshing' == j
            or
            'reliable' == j
            or
            'respectable' == j
            or
            'revolutionary' == j
            or
            'rewarding' == j
            or
            'rousing' == j
            or
            'saintly' == j
            or
            'salubrious' == j
            or
            'satisfying' == j
            or
            'scrumptious' == j
            or
            'sensational' == j
            or
            'sexy' == j
            or
            'shiny' == j
            or
            'showy' == j
            or
            'smashing' == j
            or
            'soothing' == j
            or
            'sought-after' == j
            or
            'spectacular' == j
            or
            'spiffy' == j
            or
            'stimulating' == j
            or
            'striking' == j
            or
            'stunning' == j
            or
            'stupendous' == j
            or
            'superb' == j
            or
            'supreme' == j
            or
            'swanky' == j
            or
            'tasteful' == j
            or
            'tasty' == j
            or
            'terrific' == j
            or
            'thrilling' == j
            or
            'titillating' == j
            or
            'tremendous' == j
            or
            'trusty' == j
            or
            'ultimate' == j
            or
            'unbelievable' == j
            or
            'uplifting' == j
            or
            'useful' == j
            or
            'valuable' == j
            or
                'vibrant' == j):
            p += 1
        elif ("fuck" == j or 
        'abnormal' == j or 
        'abolish' == j or
              'abominable' == j or
              'abominably' == j or
              'abominate' == j or
              'abomination' == j or
              'abort' == j or
              'aborted' == j or
              'aborts' == j or
              'abrade' == j or
              'abrasive' == j or
              'abrupt' == j or
              'abruptly' == j or
              'abscond' == j or
              'absence' == j or
              'absent-minded' == j or
              'absentee' == j or
              'absurd' == j or
              'absurdity' == j or
              'absurdly' == j or
              'absurdness' == j or
              'abuse' == j or
              'abused' == j or
              'abuses' == j or
              'abusive' == j or
              'abysmal' == j or
              'abysmally' == j or
              'abyss' == j or
              'accidental' == j or
              'accost' == j or
              'accursed' == j or
              'accusation' == j or
              'accusations' == j or
              'accuse' == j or
              'accuses' == j or
              'accusing' == j or
              'accusingly' == j or
              'acerbate' == j or
              'acerbic' == j or
              'acerbically' == j or
              'ache' == j or 'ached' == j or
              'aches' == j or
              'aching' == j or
              'acrid' == j or
              'acridly' == j or
              'acridness' == j or
              'acrimonious' == j or
              'acrimoniously' == j or 'acrimony' == j or
              'adamant' == j or
              'adamantly' == j or
              'addict' == j or
              'addicted' == j or
              'addicting' == j or
              'addicts' == j or
              'admonish' == j or 'admonisher' == j or
              'admonishingly' == j or
              'admonishment' == j or
              'admonition' == j or
              'adulterate' == j or
              'adulterated' == j or
              'adulteration' == j or 'adversarial' == j or
              'adversary' == j or
              'adverse' == j or
              'adversity' == j or
              'afflict' == j or
              'affliction' == j or
              'afflictive' == j or
              'affront' == j or 'afraid' == j or
              'aggravate' == j or
              'aggravating' == j or
              'aggravation' == j or
              'aggression' == j or
              'aggressive' == j or 'aggressiveness' == j or
              'aggressor' == j or
              'aggrieve' == j or
              'aggrieved' == j or
              'aghast' == j or
              'agonies' == j or
              'agonize' == j or 'agonizing' == j or
              'agonizingly' == j or
              'agony' == j or
              'aground' == j or
              'ail' == j or
              'ailing' == j or
              'ailment' == j or 'aimless' == j or
              'alarm' == j or
              'alarmed' == j or
              'alarming' == j or
              'alarmingly' == j or
              'alienate' == j or 'alienated' == j or
              'alienation' == j or
              'allegation' == j or
              'allegations' == j or
              'allege' == j or 'allergic' == j or
              'allergies' == j or
              'allergy' == j or
              'aloof' == j or
              'altercation' == j or
              'ambiguity' == j or
              'ambiguous' == j or
              'ambivalence' == j or
              'ambivalent' == j or
              'ambush' == j or
              'amiss' == j or
              'amputate' == j or
              'anarchism' == j or
              'anarchist' == j or
              'anarchistic' == j or
              'anarchy' == j or
              'anemic' == j or
              'anger' == j or
              'angrily' == j or
              'angriness' == j or
              'angry' == j or
              'anguish' == j or
              'animosity' == j or
              'annihilate' == j or
              'annihilation' == j or
              'annoy' == j or
              'annoyance' == j or
              'annoyances' == j or
              'annoyed' == j or
              'annoying' == j or
              'annoyingly' == j or
              'annoys' == j or
              'anomalous' == j or
              'anomaly' == j or
              'antagonism' == j or
              'antagonist' == j or
              'antagonistic' == j or
              'antagonize' == j or
              'anti-' == j or
              'anti-occupation' == j or
              'anti-proliferation' == j or
              'anti-social' == j or
              'anti-us' == j or
              'anti-white' == j or
              'antipathy' == j or
              'antiquated' == j or
              'antithetical' == j or
              'anxieties' == j or
              'anxiety' == j or
              'anxious' == j or
              'anxiously' == j or
              'anxiousness' == j or
              'apathetic' == j or
              'apathetically' == j or
              'apathy' == j or
              'apocalypse' == j or
              'apocalyptic' == j or
              'apologist' == j or
              'apologists' == j or
              'appall' == j or
              'appalled' == j or
              'appalling' == j or
              'appallingly' == j or
              'apprehension' == j or
              'apprehensions' == j or
              'apprehensive' == j or
              'apprehensively' == j or
              'arbitrary' == j or
              'arcane' == j or
              'archaic' == j or
              'arduous' == j or
              'arduously' == j or
              'argumentative' == j or
              'arrogance' == j or
              'arrogant' == j or
              'arrogantly' == j or
              'ashamed' == j or
              'asinine' == j or
              'asininely' == j or
              'askance' == j or
              'asperse' == j or
              'aspersion' == j or
              'aspersions' == j or
              'assail' == j or
              'assassin' == j or
              'assassinate' == j or
              'assault' == j or
              'astray' == j or
              'asunder' == j or
              'atrocious' == j or
              'atrocities' == j or
              'atrocity' == j or
              'atrophy' == j or
              'attack' == j or
              'attacks' == j or
              'audacious' == j or
              'audaciously' == j or
              'audaciousness' == j or
              'audacity' == j or
              'austere' == j or
              'authoritarian' == j or
              'autocrat' == j or
              'autocratic' == j or
              'avalanche' == j or
              'avarice' == j or
              'avaricious' == j or
              'avariciously' == j or
              'avenge' == j or
              'averse' == j or
              'aversion' == j or
              'awful' == j or
              'awfully' == j or
              'awfulness' == j or
              'awkward' == j or
              'awkwardness,babble' == j or
              'back-logged' == j or
              'back-wood' == j or
              'back-woods' == j or
              'backache' == j or
              'backaches' == j or
              'backbite' == j or
              'backbiting' == j or
              'backward' == j or
              'backwardness' == j or
              'backwoods' == j or
              'bad' == j or
              'badly' == j or
              'baffle' == j or
              'baffled' == j or
              'bafflement' == j or
              'baffling' == j or
              'bait' == j or
              'balk' == j or
              'banal' == j or
              'bane' == j or
              'banish' == j or
              'banishment' == j or
              'bankrupt' == j or
              'barbarian' == j or
              'barbaric' == j or
              'barbarically' == j or
              'barbarity' == j or
              'barbarous' == j or
              'barbarously' == j or
              'barren' == j or
              'baseless' == j or
              'bash' == j or
              'bashed' == j or
              'bashful' == j or
              'bashing' == j or
              'battered' == j or
              'battering' == j or
              'batty' == j or
              'bearish' == j or
              'beastly' == j or
              'bedlam' == j or
              'bedlamite' == j or
              'befoul' == j or
              'beg' == j or
              'beggar' == j or
              'beggarly' == j or
              'begging' == j or
              'beguile' == j or
              'belabor' == j or
              'belated' == j or
              'beleaguer' == j or
              'belie' == j or
              'belittle' == j or
              'belittled' == j or
              'belittling' == j or
              'bellicose' == j or
              'belligerence' == j or
              'belligerent' == j or
              'belligerently' == j or
              'bemoan' == j or
              'bemoaning' == j or
              'bemused' == j or
              'bent' == j or
              'berate' == j or
              'bereave' == j or
              'bereavement' == j or
              'bereft' == j or
              'berserk' == j or
              'beseech' == j or
              'beset' == j or
              'besiege' == j or
              'besmirch' == j or
              'betray' == j or
              'betrayal' == j or
              'betrayals' == j or
              'betrayer' == j or
              'betraying' == j or
              'betrays' == j or
              'bewail' == j or
              'beware' == j or
              'bewilder' == j or
              'bewildered' == j or
              'bewildering' == j or
              'bewilderingly' == j or
              'bewilderment' == j or
              'bewitch' == j or
              'bias' == j or
              'biased' == j or
              'biases' == j or
              'bicker' == j or
              'bickering' == j or
              'bid-rigging' == j or
              'bigotries' == j or
              'bigotry' == j or
              'biting' == j or
              'bitingly' == j or
              'bitter' == j or
              'bitterly' == j or
              'bitterness' == j or
              'bizarre' == j or
              'blab' == j or
              'blabber' == j or
              'blackmail' == j or
              'blah' == j or
              'blame' == j or
              'blameworthy' == j or
              'bland' == j or
              'blandish' == j or
              'blaspheme' == j or
              'blasphemous' == j or
              'blasphemy' == j or
              'blasted' == j or
              'blatant' == j or
              'blatantly' == j or
              'blather' == j or
              'bleak' == j or
              'bleakly' == j or
              'bleakness' == j or
              'bleed' == j or
              'bleeding' == j or
              'bleeds' == j or
              'blemish' == j or
              'blind' == j or
              'blinding' == j or
              'blindingly' == j or
              'blindside' == j or
              'blister' == j or
              'blistering' == j or
              'bloated' == j or
              'blockage' == j or
              'blockhead' == j or
              'bloodshed' == j or
              'bloodthirsty' == j or
              'bloody' == j or
              'blotchy' == j or
              'blow' == j or
              'blunder' == j or
              'blundering' == j or
              'blunders' == j or
              'blunt' == j or
              'blur' == j or
              'blurred' == j or
              'blurring' == j or
              'blurry' == j or
              'blurs' == j or
              'blurt' == j or
              'boastful' == j or
              'boggle' == j or
              'bogus' == j or
              'boil' == j or
              'boiling' == j or
              'boisterous' == j or
              'bomb' == j or
              'bombard' == j or
              'bombardment' == j or
              'bombastic' == j or
              'bondage' == j or
              'bonkers' == j or
              'bore' == j or
              'bored' == j or
              'boredom' == j or
              'bores' == j or
              'boring' == j or
              'botch' == j or
              'bother' == j or
              'bothered' == j or
              'bothering' == j or
              'bothers' == j or
              'bothersome' == j or
              'bowdlerize' == j or
              'boycott' == j or
              'braggart' == j or
              'bragger' == j or
              'brainless' == j or
              'brainwash' == j or
              'brash' == j or
              'brashly' == j or
              'brashness' == j or
              'brat' == j or
              'bravado' == j or
              'brazen' == j or
              'brazenly' == j or
              'brazenness' == j or
              'breach' == j or
              'break' == j or
              'break-up' == j or
              'break-ups' == j or
              'breakdown' == j or
              'breaking' == j or
              'breaks' == j or
              'breakup' == j or
              'breakups' == j or
              'bribery' == j or
              'brimstone' == j or
              'bristle' == j or
              'brittle' == j or
              'broke' == j or
              'broken' == j or
              'broken-hearted' == j or
              'brood' == j or
              'browbeat' == j or
              'bruise' == j or
              'bruised' == j or
              'bruises' == j or
              'bruising' == j or
              'brusque' == j or
              'brutal' == j or
              'brutalities' == j or
              'brutality' == j or
              'brutalize' == j or
              'brutalizing' == j or
              'brutally' == j or
              'brute' == j or
              'brutish' == j or
              'buckle' == j or
              'bug' == j or
              'bugging' == j or
              'buggy' == j or
              'bugs' == j or
              'bulkier' == j or
              'bulkiness' == j or
              'bulky' == j or
              'bull****' == j or
              'bullshit' == j or
              'bullies' == j or
              'bulls..t' == j or
              'bully' == j or
              'bullying' == j or
              'bullyingly' == j or
              'bum' == j or
              'bump' == j or
              'bumped' == j or
              'bumping' == j or
              'bumps' == j or
              'bumpy' == j or
              'bungle' == j or
              'bungler' == j or
              'bungling' == j or
              'bunk' == j or
              'burden' == j or
              'burdensome' == j or
              'burdensomely' == j or
              'burn' == j or
              'burned' == j or
              'burning' == j or
              'burns' == j or
              'bust' == j or
              'busts' == j or
              'busybody' == j or
              'butcher' == j or
              'butchery' == j or
              'buzzing,cackle' == j or
              'calamities' == j or
              'calamitous' == j or
              'calamitously' == j or
              'calamity' == j or
              'callous' == j or
              'calumniate' == j or
              'calumniation' == j or
              'calumnies' == j or
              'calumnious' == j or
              'calumniously' == j or
              'calumny' == j or
              'cancer' == j or
              'cancerous' == j or
              'cannibal' == j or
              'cannibalize' == j or
              'capitulate' == j or
              'capricious' == j or
              'capriciously' == j or
              'capriciousness' == j or
              'capsize' == j or
              'careless' == j or
              'carelessness' == j or
              'caricature' == j or
              'carnage' == j or
              'carp' == j or
              'cartoonish' == j or
              'cash-strapped' == j or
              'castigate' == j or
              'castrated' == j or
              'casualty' == j or
              'cataclysm' == j or
              'cataclysmal' == j or
              'cataclysmic' == j or
              'cataclysmically' == j or
              'catastrophe' == j or
              'catastrophes' == j or
              'catastrophic' == j or
              'catastrophically' == j or
              'caustic' == j or
              'caustically' == j or
              'cautionary' == j or
              'cave' == j or
              'censure' == j or
              'chafe' == j or
              'chaff' == j or
              'chagrin' == j or
              'challenging' == j or
              'chaos' == j or
              'chaotic' == j or
              'chasten' == j or
              'chastise' == j or
              'chastisement' == j or
              'chatter' == j or
              'chatterbox' == j or
              'cheap' == j or
              'cheapen' == j or
              'cheaply' == j or
              'cheat' == j or
              'cheated' == j or
              'cheater' == j or
              'cheating' == j or
              'cheats' == j or
              'checkered' == j or
              'cheerless' == j or
              'cheesy' == j or
              'chide' == j or
              'childish' == j or
              'chill' == j or
              'chilly' == j or
              'chintzy' == j or
              'choke' == j or
              'choleric' == j or
              'choppy' == j or
              'chore' == j or
              'chronic' == j or
              'chunky' == j or
              'clamor' == j or
              'clamorous' == j or
              'clash' == j or
              'clique' == j or
              'clog' == j or
              'clogged' == j or
              'clogs' == j or
              'cloud' == j or
              'clouding' == j or
              'cloudy' == j or
              'clueless' == j or
              'clumsy' == j or
              'clunky' == j or
              'coarse' == j or
              'cocky' == j or
              'coerce' == j or
              'coercion' == j or
              'coercive' == j or
              'cold' == j or
              'coldly' == j or
              'collapse' == j or
              'collude' == j or
              'collusion' == j or
              'combative' == j or
              'combust' == j or
              'comical' == j or
              'commiserate' == j or
              'commonplace' == j or
              'commotion' == j or
              'commotions' == j or
              'complacent' == j or
              'complain' == j or
              'complained' == j or
              'complaining' == j or
              'complains' == j or
              'complaint' == j or
              'complaints' == j or
              'complex' == j or
              'complicated' == j or
              'complication' == j or
              'complicit' == j or
              'compulsion' == j or
              'compulsive' == j or
              'concede' == j or
              'conceded' == j or
              'conceit' == j or
              'conceited' == j or
              'concern' == j or
              'concerned' == j or
              'concerns' == j or
              'concession' == j or
              'concessions' == j or
              'condemn' == j or
              'condemnable' == j or
              'condemnation' == j or
              'condemned' == j or
              'condemns' == j or
              'condescend' == j or
              'condescending' == j or
              'condescendingly' == j or
              'condescension' == j or
              'confess' == j or
              'confession' == j or
              'confessions' == j or
              'confined' == j or
              'conflict' == j or
              'conflicted' == j or
              'conflicting' == j or
              'conflicts' == j or
              'confound' == j or
              'confounded' == j or
              'confounding' == j or
              'confront' == j or
              'confrontation' == j or
              'confrontational' == j or
              'confuse' == j or
              'confused' == j or
              'confuses' == j or
              'confusing' == j or
              'confusion' == j or
              'confusions' == j or
              'congested' == j or
              'congestion' == j or
              'cons' == j or
              'conservative' == j or
              'conspicuous' == j or
              'conspicuously' == j or
              'conspiracies' == j or
              'conspiracy' == j or
              'conspirator' == j or
              'conspiratorial' == j or
              'conspire' == j or
              'consternation' == j or
              'contagious' == j or
              'contaminate' == j or
              'contaminated' == j or
              'contaminates' == j or
              'contaminating' == j or
              'contamination' == j or
              'contempt' == j or
              'contemptible' == j or
              'contemptuous' == j or
              'contemptuously' == j or
              'contend' == j or
              'contention' == j or
              'contentious' == j or
              'contort' == j or
              'contortions' == j or
              'contradict' == j or
              'contradiction' == j or
              'contradictory' == j or
              'contrariness' == j or
              'contravene' == j or
              'contrive' == j or
              'contrived' == j or
              'controversial' == j or
              'controversy' == j or
              'convoluted' == j or
              'corrode' == j or
              'corrosion' == j or
              'corrosions' == j or
              'corrosive' == j or
              'corrupt' == j or
              'corrupted' == j or
              'corrupting' == j or
              'corruption' == j or
              'corrupts' == j or
              'costlier' == j or
              'costly' == j or
              'counter-productive' == j or
              'counterproductive' == j or
              'covetous' == j or
              'coward' == j or
              'cowardly' == j or
              'crabby' == j or
              'crack' == j or
              'cracked' == j or
              'cracks' == j or
              'craftily' == j or
              '   crafty' == j or
              'cramp' == j or
              'cramped' == j or
              'cramping' == j or
              'cranky' == j or
              'crap' == j or
              'crappy' == j or
              'craps' == j or
              'crash' == j or
              'crashed' == j or
              'crashes' == j or
              'crashing' == j or
              'crass' == j or
              'craven' == j or
              'cravenly' == j or
              'craze' == j or
              'crazily' == j or
              'craziness' == j or
              'crazy' == j or
              'creak' == j or
              'creaking' == j or
              'creaks' == j or
              'credulous' == j or
              'creep' == j or
              'creeping' == j or
              'creeps' == j or
              'creepy' == j or
              'crept' == j or
              'crime' == j or
              'criminal' == j or
              'cringe' == j or
              'cringed' == j or
              'cringes' == j or
              'cripple' == j or
              'crippled' == j or
              'cripples' == j or
              'crippling' == j or
              'crisis' == j or
              'critic' == j or
              'critical' == j or
              'criticism' == j or
              'criticisms' == j or
              'criticize' == j or
              'criticized' == j or
              'criticizing' == j or
              'critics' == j or
              'cronyism' == j or
              'crook' == j or
              'crooked' == j or
              'crooks' == j or
              'crowded' == j or
              'crowdedness' == j or
              'crude' == j or
              'cruel' == j or
              'crueler' == j or
              'cruelest' == j or
              'cruelly' == j or
              'cruelness' == j or
              'cruelties' == j or
              'cruelty' == j or
              'crumble' == j or
              'crumbling' == j or
              'crummy' == j or
              'crumple' == j or
              'crumpled' == j or
              'crumples' == j or
              'crush' == j or
              'crushed' == j or
              'crushing' == j or
              'cry' == j or
              'culpable' == j or
              'culprit' == j or
              'cumbersome' == j or
              'curse' == j or
              'cursed' == j or
              'curses' == j or
              'curt' == j or
              'cuss' == j or
              'cussed' == j or
              'cutthroat' == j or
              'cynical,damage' == j or
              'damaged' == j or
              'damages' == j or
              'damaging' == j or
              'damn' == j or
              'damnable' == j or
              'damnably' == j or
              'damnation' == j or
              'damned' == j or
              'damning' == j or
              'damper' == j or
              'danger' == j or
              'dangerous' == j or
              'dangerousness' == j or
              'dark' == j or
              'darken' == j or
              'darkened' == j or
              'darker' == j or
              'darkness' == j or
              'dastard' == j or
              'dastardly' == j or
              'daunt' == j or
              'daunting' == j or
              'dauntingly' == j or
              'dawdle' == j or
              'daze' == j or
              'dazed' == j or
              'dead' == j or
              'deadbeat' == j or
              'deadlock' == j or
              'deadly' == j or
              'deadweight' == j or
              'deaf' == j or
              'dearth' == j or
              'death' == j or
              'debacle' == j or
              'debase' == j or
              'debasement' == j or
              'debaser' == j or
              'debatable' == j or
              'debauch' == j or
              'debaucher' == j or
              'debauchery' == j or
              'debilitate' == j or
              'debilitating' == j or
              'debility' == j or
              'debt' == j or
              'debts' == j or
              'decadence' == j or
              'decadent' == j or
              'decay' == j or
              'decayed' == j or
              'deceit' == j or
              'deceitful' == j or
              'deceitfully' == j or
              'deceitfulness' == j or
              'deceive' == j or
              'deceiver' == j or
              'deceivers' == j or
              'deceiving' == j or
              'deception' == j or
              'deceptive' == j or
              'deceptively' == j or
              'declaim' == j or
              'decline' == j or
              'declines' == j or
              'declining' == j or
              'decrement' == j or
              'decrepit' == j or
              'decrepitude' == j or
              'decry' == j or
              'defamation' == j or
              'defamations' == j or
              'defamatory' == j or
              'defame' == j or
              'defect' == j or
              'defective' == j or
              'defects' == j or
              'defensive' == j or
              'defiance' == j or
              'defiant' == j or
              'defiantly' == j or
              'deficiencies' == j or
              'deficiency' == j or
              'deficient' == j or
              'defile' == j or
              'defiler' == j or
              'deform' == j or
              'deformed' == j or
              'defrauding' == j or
              'defunct' == j or
              'defy' == j or
              'degenerate' == j or
              'degenerately' == j or
              'degeneration' == j or
              'degradation' == j or
              'degrade' == j or
              'degrading' == j or
              'degradingly' == j or
              'dehumanization' == j or
              'dehumanize' == j or
              'deign' == j or
              'deject' == j or
              'dejected' == j or
              'dejectedly' == j or
              'dejection' == j or
              'delay' == j or
              'delayed' == j or
              'delaying' == j or
              'delays' == j or
              'delinquency' == j or
              'delinquent' == j or
              'delirious' == j or
              'delirium' == j or
              'delude' == j or
              'deluded' == j or
              'deluge' == j or
              'delusion' == j or
              'delusional' == j or
              'delusions' == j or
              'demean' == j or
              'demeaning' == j or
              'demise' == j or
              'demolish' == j or
              'demolisher' == j or
              'demon' == j or
              'demonic' == j or
              'demonize' == j or
              'demonized' == j or
              'demonizes' == j or
              'demonizing' == j or
              'demoralize' == j or
              'demoralizing' == j or
              'demoralizingly' == j or
              'denial' == j or
              'denied' == j or
              'denies' == j or
              'denigrate' == j or
              'denounce' == j or
              'dense' == j or
              'dent' == j or
              'dented' == j or
              'dents' == j or
              'denunciate' == j or
              'denunciation' == j or
              'denunciations' == j or
              'deny' == j or
              'denying' == j or
              'deplete' == j or
              'deplorable' == j or
              'deplorably' == j or
              'deplore' == j or
              'deploring' == j or
              'deploringly' == j or
              'deprave' == j or
              'depraved' == j or
              'depravedly' == j or
              'deprecate' == j or
              'depress' == j or
              'depressed' == j or
              'depressing' == j or
              'depressingly' == j or
              'depression' == j or
              'depressions' == j or
              'deprive' == j or
              'deprived' == j or
              'deride' == j or
              'derision' == j or
              'derisive' == j or
              'derisively' == j or
              'derisiveness' == j or
              'derogatory' == j or
              'desecrate' == j or
              'desert' == j or
              'desertion' == j or
              'desiccate' == j or
              'desiccated' == j or
              'desolate' == j or
              'desolately' == j or
              'desolation' == j or
              'despair' == j or
              'despairing' == j or
              'despairingly' == j or
              'desperate' == j or
              'desperately' == j or
              'desperation' == j or
              'despicable' == j or
              'despicably' == j or
              'despise' == j or
              'despised' == j or
              'despoil' == j or
              'despoiler' == j or
              'despondence' == j or
              'despondency' == j or
              'despondent' == j or
              'despondently' == j or
              'despot' == j or
              'despotic' == j or
              'despotism' == j or
              'destitute' == j or
              'destitution' == j or
              'destroy' == j or
              'destroyer' == j or
              'destruction' == j or
              'destructive' == j or
              'desultory' == j or
              'deter' == j or
              'deteriorate' == j or
              'deteriorating' == j or
              'deterioration' == j or
              'deterrent' == j or
              'detest' == j or
              'detestable' == j or
              'detestably' == j or
              'detested' == j or
              'detesting' == j or
              'detests' == j or
              'detract' == j or
              'detracted' == j or
              'detracting' == j or
              'detraction' == j or
              'detracts' == j or
              'detriment' == j or
              'detrimental' == j or
              'devastate' == j or
              'devastated' == j or
              'devastates' == j or
              'devastating' == j or
              'devastatingly' == j or
              'devastation' == j or
              'deviate' == j or
              'deviation' == j or
              'devil' == j or
              'devilish' == j or
              'devilishly' == j or
              'devilment' == j or
              'devilry' == j or
              'devious' == j or
              'deviously' == j or
              'deviousness' == j or
              'devoid' == j or
              'diabolic' == j or
              'diabolical' == j or
              'diabolically' == j or
              'diametrically' == j or
              'diatribe' == j or
              'diatribes' == j or
              'dick' == j or
              'dictator' == j or
              'dictatorial' == j or
              'die' == j or
              'die-hard' == j or
              'died' == j or
              'dies' == j or
              'difficult' == j or
              'difficulties' == j or
              'difficulty' == j or
              'diffidence' == j or
              'dilapidated' == j or
              'dilemma' == j or
              'dilly-dally' == j or
              'dim' == j or
              'dimmer' == j or
              'ding' == j or
              'dings' == j or
              'dinky' == j or
              'dire' == j or
              'direly' == j or
              'direness' == j or
              'dirt' == j or
              'dirty' == j or
              'disable' == j or
              'disabled' == j or
              'disaccord' == j or
              'disadvantage' == j or
              'disadvantaged' == j or
              'disadvantageous' == j or
              'disadvantages' == j or
              'disaffect' == j or
              'disaffected' == j or
              'disaffirm' == j or
              'disagree' == j or
              'disagreeable' == j or
              'disagreeably' == j or
              'disagreed' == j or
              'disagreeing' == j or
              'disagreement' == j or
              'disagrees' == j or
              'disallow' == j or
              'disappoint' == j or
              'disappointed' == j or
              'disappointing' == j or
              'disappointingly' == j or
              'disappointment' == j or
              'disappointments' == j or
              'disappoints' == j or
              'disapprobation' == j or
              'disapproval' == j or
              'disapprove' == j or
              'disapproving' == j or
              'disarm' == j or
              'disarray' == j or
              'disaster' == j or
              'disastrous' == j or
              'disastrously' == j or
              'disavow' == j or
              'disavowal' == j or
              'disbelief' == j or
              'disbelieve' == j or
              'disbeliever' == j or
              'disclaim' == j or
              'discombobulate' == j or
              'discomfit' == j or
              '   discomfort' == j or
              'discompose' == j or
              'disconcert' == j or
              'disconcerted' == j or
              'disconcerting' == j or
              'disconcertingly' == j or
              'disconsolate' == j or
              'disconsolately' == j or
              'disconsolation' == j or
              'discontent' == j or
              'discontented' == j or
              'discontentedly' == j or
              'discontinued' == j or
              'discontinuity' == j or
              'discontinuous' == j or
              'discord' == j or
              'discordance' == j or
              'discordant' == j or
              'discountenance' == j or
              'discourage' == j or
              'discouragement' == j or
              'discouraging' == j or
              'discouragingly' == j or
              'discourteous' == j or
              'discourteously' == j or
              'discredit' == j or
              'discrepant' == j or
              'discriminate' == j or
              'discrimination' == j or
              'discriminatory' == j or
              'disdain' == j or
              'disdained' == j or
              'disdainful' == j or
              'disdainfully' == j or
              'disfavor' == j or
              'disgrace' == j or
              'disgraced' == j or
              'disgraceful' == j or
              'disgracefully' == j or
              'disgruntle' == j or
              'disgruntled' == j or
              'disgust' == j or
              'disgusted' == j or
              'disgustedly' == j or
              'disgustful' == j or
              'disgustfully' == j or
              'disgusting' == j or
              'disgustingly' == j or
              'dishearten' == j or
              'disheartening' == j or
              'dishearteningly' == j or
              'dishonest' == j or
              'dishonestly' == j or
              'dishonesty' == j or
              'dishonor' == j or
              'dishonorable' == j or
              'disillusion' == j or
              'disillusioned' == j or
              'disillusionment' == j or
              'disillusions' == j or
              'disinclination' == j or
              'disinclined' == j or
              'disingenuous' == j or
              'disingenuously' == j or
              'disintegrate' == j or
              'disintegrated' == j or
              'disintegrates' == j or
              'disintegration' == j or
              'disinterest' == j or
              'disinterested' == j or
              'dislike' == j or
              'disliked' == j or
              'dislikes' == j or
              'disliking' == j or
              'dislocated' == j or
              'disloyal' == j or
              'disloyalty' == j or
              'dismal' == j or
              'dismally' == j or
              'dismalness' == j or
              'dismay' == j or
              'dismayed' == j or
              'dismaying' == j or
              'dismayingly' == j or
              'dismissive' == j or
              'dismissively' == j or
              'disobedience' == j or
              'disobedient' == j or
              'disobey' == j or
              'disorder' == j or
              'disordered' == j or
              'disorderly' == j or
              'disorganized' == j or
              'disorient' == j or
              'disoriented' == j or
              'disown' == j or
              'disparage' == j or
              'disparaging' == j or
              'disparagingly' == j or
              'dispensable' == j or
              'dispirit' == j or
              'dispirited' == j or
              'dispiritedly' == j or
              'dispiriting' == j or
              'displace' == j or
              'displaced' == j or
              'displease' == j or
              'displeased' == j or
              'displeasing' == j or
              'displeasure' == j or
              'disproportionate' == j or
              'disprove' == j or
              'disputable' == j or
              'dispute' == j or
              'disputed' == j or
              'disquiet' == j or
              'disquieting' == j or
              'disquietingly' == j or
              'disquietude' == j or
              'disregard' == j or
              'disregardful' == j or
              'disreputable' == j or
              'disrepute' == j or
              'disrespect' == j or
              'disrespectable' == j or
              'disrespectful' == j or
              'disrespectfully' == j or
              'disrespectfulness' == j or
              'disrespecting' == j or
              'disrupt' == j or
              'disruption' == j or
              'disruptive' == j or
              'dissatisfaction' == j or
              'dissatisfactory' == j or
              'dissatisfied' == j or
              'dissatisfies' == j or
              'dissatisfy' == j or
              'dissatisfying' == j or
              'dissed' == j or
              'dissemble' == j or
              'dissembler' == j or
              'dissension' == j or
              'dissent' == j or
              'dissenter' == j or
              'dissention' == j or
              'disservice' == j or
              'disses' == j or
              'dissidence' == j or
              'dissident' == j or
              'dissidents' == j or
              'dissing' == j or
              'dissocial' == j or
              'dissolute' == j or
              'dissolution' == j or
              'dissonance' == j or
              'dissonant' == j or
              'dissonantly' == j or
              'dissuade' == j or
              'dissuasive' == j or
              'distains' == j or
              'distaste' == j or
              'distasteful' == j or
              'distastefully' == j or
              'distort' == j or
              'distorted' == j or
              'distortion' == j or
              'distorts' == j or
              'distract' == j or
              'distracting' == j or
              'distraction' == j or
              'distraught' == j or
              'distraughtly' == j or
              'distress' == j or
              'distressed' == j or
              'distressing' == j or
              'distressingly' == j or
              'distrust' == j or
              'distrustful' == j or
              'distrusting' == j or
              'disturb' == j or
              'disturbance' == j or
              'disturbed' == j or
              'disturbing' == j or
              'disturbingly' == j or
              'disunity' == j or
              'disvalue' == j or
              'divergent' == j or
              'divisive' == j or
              'divisively' == j or
              'divisiveness' == j or
              'dizzy' == j or
              'doddering' == j or
              'dogged' == j or
              'doggedly' == j or
              'dogmatic' == j or
              'doldrums' == j or
              'domineer' == j or
              'domineering' == j or
              'doom' == j or
              'doomed' == j or
              'doomsday' == j or
              'dope' == j or
              'doubt' == j or
              'doubtful' == j or
              'doubtfully' == j or
              'doubts' == j or
              'douchebag' == j or
              'douchebags' == j or
              'downbeat' == j or
              'downcast' == j or
              'downer' == j or
              'downfall' == j or
              'downfallen' == j or
              'downgrade' == j or
              'downhearted' == j or
              'downheartedly' == j or
              'downhill' == j or
              'downside' == j or
              'downsides' == j or
              'downturn' == j or
              'downturns' == j or
              'drab' == j or
              'draconian' == j or
              'draconic' == j or
              'drag' == j or
              'dragged' == j or
              'dragging' == j or
              'dragoon' == j or
              'drags' == j or
              'drain' == j or
              'drained' == j or
              'draining' == j or
              'drains' == j or
              'drastic' == j or
              'drastically' == j or
              'drawback' == j or
              'drawbacks' == j or
              'dread' == j or
              'dreadful' == j or
              'dreadfully' == j or
              'dreadfulness' == j or
              'dreary' == j or
              'dripped' == j or
              'dripping' == j or
              'drippy' == j or
              'drips' == j or
              'drones' == j or
              'droop' == j or
              'droops' == j or
              'drop-out' == j or
              'drop-outs' == j or
              'dropout' == j or
              'dropouts' == j or
              'drought' == j or
              'drowning' == j or
              'drunk' == j or
              'drunkard' == j or
              'drunken' == j or
              'dubious' == j or
              'dubiously' == j or
              'dubitable' == j or
              'dud' == j or
              'dull' == j or
              'dullard' == j or
              'dumb' == j or
              'dumbfound' == j or
              'dump' == j or
              'dumped' == j or
              'dumping' == j or
              'dumps' == j or
              'dunce' == j or
              'dungeon' == j or
              'dungeons' == j or
              'dupe' == j or
              'dust' == j or
              'dusty' == j or
              'dwindling,earsplitting' == j or
              'eccentric' == j or
              'eccentricity' == j or
              'effigy' == j or
              'effrontery' == j or
              'egocentric' == j or
              'egomania' == j or
              'egotism' == j or
              'egotistical' == j or
              'egotistically' == j or
              'egregious' == j or
              'egregiously' == j or
              'election-rigger' == j or
              'elimination' == j or
              'emaciated' == j or
              'emasculate' == j or
              'embarrass' == j or
              'embarrassing' == j or
              'embarrassingly' == j or
              'embarrassment' == j or
              'embattled' == j or
              'embroil' == j or
              'embroiled' == j or
              'embroilment' == j or
              'emergency' == j or
              'emphatic' == j or
              'emphatically' == j or
              'emptiness' == j or
              'encroach' == j or
              'encroachment' == j or
              'endanger' == j or
              'enemies' == j or
              'enemy' == j or
              'enervate' == j or
              'enfeeble' == j or
              'enflame' == j or
              'engulf' == j or
              'enjoin' == j or
              'enmity' == j or
              'enrage' == j or
              'enraged' == j or
              'enraging' == j or
              'enslave' == j or
              'entangle' == j or
              'entanglement' == j or
              'entrap' == j or
              'entrapment' == j or
              'envious' == j or
              'enviously' == j or
              'enviousness' == j or
              'epidemic' == j or
              'equivocal' == j or
              'erase' == j or
              'erode' == j or
              'erodes' == j or
              'erosion' == j or
              'err' == j or
              'errant' == j or
              'erratic' == j or
              'erratically' == j or
              'erroneous' == j or
              'erroneously' == j or
              'error' == j or
              'errors' == j or
              'eruptions' == j or
              'escapade' == j or
              'eschew' == j or
              'estranged' == j or
              'evade' == j or
              'evasion' == j or
              'evasive' == j or
              'evil' == j or
              'evildoer' == j or
              'evils' == j or
              'eviscerate' == j or
              'exacerbate' == j or
              'exaggerate' == j or
              'exaggeration' == j or
              'exasperate' == j or
              'exasperated' == j or
              'exasperating' == j or
              'exasperatingly' == j or
              'exasperation' == j or
              'excessive' == j or
              'excessively' == j or
              'exclusion' == j or
              'excoriate' == j or
              'excruciating' == j or
              'excruciatingly' == j or
              'excuse' == j or
              'excuses' == j or
              'execrate' == j or
              'exhaust' == j or
              'exhausted' == j or
              'exhaustion' == j or
              'exhausts' == j or
              '   exhort' == j or
              'exile' == j or
              'exorbitant' == j or
              'exorbitantly' == j or
              'expel' == j or
              'expensive' == j or
              'expire' == j or
              'expired' == j or
              'explode' == j or
              'exploit' == j or
              'exploitation' == j or
              'explosive' == j or
              'expropriate' == j or
              'expropriation' == j or
              'expulse' == j or
              'expunge' == j or
              'exterminate' == j or
              'extermination' == j or
              'extinguish' == j or
              'extort' == j or
              'extortion' == j or
              'extraneous' == j or
              'extravagance' == j or
              'extravagant' == j or
              'extravagantly' == j or
              'extremism' == j or
              'extremist' == j or
              'extremists,f**k' == j or
              'fabricate' == j or
              'fabrication' == j or
              'facetious' == j or
              'facetiously' == j or
              'fail' == j or
              'failed' == j or
              'failing' == j or
              'fails' == j or
              'failure' == j or
              'failures' == j or
              'faint' == j or
              'fainthearted' == j or
              'faithless' == j or
              'fake' == j or
              'fall' == j or
              'fallacies' == j or
              'fallacious' == j or
              'fallaciously' == j or
              'fallaciousness' == j or
              'fallacy' == j or
              'fallen' == j or
              'falling' == j or
              'fallout' == j or
              'falls' == j or
              'FALSE' == j or
              'falsehood' == j or
              'falsely' == j or
              'falsify' == j or
              'falter' == j or
              'faltered' == j or
              'famine' == j or
              'famished' == j or
              'fanatic' == j or
              'fanatical' == j or
              'fanatically' == j or
              'fanaticism' == j or
              'fanatics' == j or
              'fanciful' == j or
              'far-fetched' == j or
              'farce' == j or
              'farcical' == j or
              'farcical-yet-provocative' == j or
              'farcically' == j or
              'farfetched' == j or
              'fascism' == j or
              'fascist' == j or
              'fastidious' == j or
              'fastidiously' == j or
              'fat' == j or
              'fat-cat' == j or
              'fat-cats' == j or
              'fatal' == j or
              'fatalistic' == j or
              'fatalistically' == j or
              'fatally' == j or
              'fateful' == j or
              'fatefully' == j or
              'fathomless' == j or
              'fatigue' == j or
              'fatigued' == j or
              'fatty' == j or
              'fatuity' == j or
              'fatuous' == j or
              'fatuously' == j or
              'fault' == j or
              'faults' == j or
              'faulty' == j or
              'fawningly' == j or
              'faze' == j or
              'fear' == j or
              'fearful' == j or
              'fearfully' == j or
              'fears' == j or
              'fearsome' == j or
              'feckless' == j or
              'feeble' == j or
              'feebleminded' == j or
              'feign' == j or
              'feint' == j or
              'fell' == j or
              'felon' == j or
              'felonious' == j or
              'ferociously' == j or
              'ferocity' == j or
              'fetid' == j or
              'fever' == j or
              'feverish' == j or
              'fevers' == j or
              'fiasco' == j or
              'fib' == j or
              'fibber' == j or
              'fickle' == j or
              'fiction' == j or
              'fictional' == j or
              'fictitious' == j or
              'fidget' == j or
              'fidgety' == j or
              'fiend' == j or
              'fiendish' == j or
              'fierce' == j or
              'figurehead' == j or
              'filth' == j or
              'filthy' == j or
              'finagle' == j or
              'finicky' == j or
              'fissures' == j or
              'fist' == j or
              'flabbergast' == j or
              'flabbergasted' == j or
              'flagging' == j or
              'flagrant' == j or
              'flagrantly' == j or
              'flair' == j or
              'flairs' == j or
              'flak' == j or
              'flake' == j or
              'flakey' == j or
              'flaking' == j or
              'flaky' == j or
              'flare' == j or
              'flares' == j or
              'flat-out' == j or
              'flaunt' == j or
              'flaw' == j or
              'flawed' == j or
              'flaws' == j or
              'flee' == j or
              'fleeing' == j or
              'fleer' == j or
              'flees' == j or
              'fleeting' == j or
              'flicker' == j or
              'flickering' == j or
              'flickers' == j or
              'flighty' == j or
              'flimflam' == j or
              'flimsy' == j or
              'flirt' == j or
              'flirty' == j or
              'floored' == j or
              'flounder' == j or
              'floundering' == j or
              'flout' == j or
              'fluster' == j or
              'foe' == j or
              'fool' == j or
              'fooled' == j or
              'foolhardy' == j or
              'foolish' == j or
              'foolishly' == j or
              'foolishness' == j or
              'forbid' == j or
              'forbidden' == j or
              'forbidding' == j or
              'forceful' == j or
              'foreboding' == j or
              'forebodingly' == j or
              'forfeit' == j or
              'forged' == j or
              'forgetful' == j or
              'forgetfully' == j or
              'forgetfulness' == j or
              'forlorn' == j or
              'forlornly' == j or
              'forsake' == j or
              'forsaken' == j or
              'forswear' == j or
              'foul' == j or
              'foully' == j or
              'foulness' == j or
              'fractious' == j or
              'fractiously' == j or
              'fracture' == j or
              'fragile' == j or
              'fragmented' == j or
              'frail' == j or
              'frantic' == j or
              'frantically' == j or
              'franticly' == j or
              'fraud' == j or
              'fraudulent' == j or
              'fraught' == j or
              'frazzle' == j or
              'frazzled' == j or
              'freak' == j or
              'freaking' == j or
              'freakish' == j or
              'freakishly' == j or
              'freaks' == j or
              'freeze' == j or
              'freezes' == j or
              'freezing' == j or
              'frenetic' == j or
              'frenetically' == j or
              'frenzied' == j or
              'frenzy' == j or
              'fret' == j or
              'fretful' == j or
              'frets' == j or
              'friction' == j or
              'frictions' == j or
              'fried' == j or
              'frigging' == j or
              'fright' == j or
              'frighten' == j or
              'frightening' == j or
              'frighteningly' == j or
              'frightful' == j or
              'frightfully' == j or
              'frigid' == j or
              'frost' == j or
              'frown' == j or
              'froze' == j or
              'frozen' == j or
              'fruitless' == j or
              'fruitlessly' == j or
              'frustrate' == j or
              'frustrated' == j or
              'frustrates' == j or
              'frustrating' == j or
              'frustratingly' == j or
              'frustration' == j or
              'frustrations' == j or
              'f”ck' == j or
              'f”cking' == j or
              'fudge' == j or
              'fugitive' == j or
              'full-blown' == j or
              'fulminate' == j or
              'fumble' == j or
              'fume' == j or
              'fumes' == j or
              'fundamentalism' == j or
              'funky' == j or
              'funnily' == j or
              'funny' == j or
              'furious' == j or
              'furiously' == j or
              'furor' == j or
              'fury' == j or
              'fuss' == j or
              'fussy' == j or
              'fustigate' == j or
              'fusty' == j or
              'futile' == j or
              'futilely' == j or
              'futility,gabble' == j or
              'gaff' == j or
              'gaffe' == j or
              'gainsay' == j or
              'gainsayer' == j or
              'gall' == j or
              'galling' == j or
              'gallingly' == j or
              'galls' == j or
              'gangster' == j or
              'gape' == j or
              'garbage' == j or
              'garish' == j or
              'gasp' == j or
              'gauche' == j or
              'gaudy' == j or
              'gawk' == j or
              'gawky' == j or
              'geezer' == j or
              'genocide' == j or
              'get-rich' == j or
              'ghastly' == j or
              'ghetto' == j or
              'ghosting' == j or
              'gibber' == j or
              'gibberish' == j or
              'gibe' == j or
              'giddy' == j or
              'gimmick' == j or
              'gimmicked' == j or
              'gimmicking' == j or
              'gimmicks' == j or
              'gimmicky' == j or
              'glare' == j or
              'glaringly' == j or
              'glib' == j or
              'glibly' == j or
              'glitch' == j or
              'glitches' == j or
              'gloatingly' == j or
              'gloom' == j or
              'gloomy' == j or
              'glower' == j or
              'glum' == j or
              'glut' == j or
              'gnawing' == j or
              'goad' == j or
              'goading' == j or
              'god-awful' == j or
              'goof' == j or
              'goofy' == j or
              'goon' == j or
              'gossip' == j or
              'graceless' == j or
              'gracelessly' == j or
              'graft' == j or
              'grainy' == j or
              'grapple' == j or
              'grate' == j or
              'grating' == j or
              'gravely' == j or
              'greasy' == j or
              'greed' == j or
              'greedy' == j or
              'grief' == j or
              'grievance' == j or
              'grievances' == j or
              'grieve' == j or
              'grieving' == j or
              'grievous' == j or
              'grievously' == j or
              'grim' == j or
              'grimace' == j or
              'grind' == j or
              'gripe' == j or
              'gripes' == j or
              'grisly' == j or
              'gritty' == j or
              'gross' == j or
              'grossly' == j or
              'grotesque' == j or
              'grouch' == j or
              'grouchy' == j or
              'groundless' == j or
              'grouse' == j or
              'growl' == j or
              'grudge' == j or
              'grudges' == j or
              'grudging' == j or
              'grudgingly' == j or
              'gruesome' == j or
              'gruesomely' == j or
              'gruff' == j or
              'grumble' == j or
              'grumpier' == j or
              'grumpiest' == j or
              'grumpily' == j or
              'grumpy' == j or
              'guile' == j or
              'guilt' == j or
              'guiltily' == j or
              'guilty' == j or
              'gullible' == j or
              'gutless,gabble' == j or
              'gaff' == j or
              'gaffe' == j or
              'gainsay' == j or
              'gainsayer' == j or
              'gall' == j or
              'galling' == j or
              'gallingly' == j or
              'galls' == j or
              'gangster' == j or
              'gape' == j or
              'garbage' == j or
              'garish' == j or
              'gasp' == j or
              'gauche' == j or
              'gaudy' == j or
              'gawk' == j or
              'gawky' == j or
              'geezer' == j or
              'genocide' == j or
              'get-rich' == j or
              'ghastly' == j or
              'ghetto' == j or
              'ghosting' == j or
              'gibber' == j or
              'gibberish' == j or
              'gibe' == j or
              'giddy' == j or
              'gimmick' == j or
              'gimmicked' == j or
              'gimmicking' == j or
              'gimmicks' == j or
              'gimmicky' == j or
              'glare' == j or
              'glaringly' == j or
              'glib' == j or
              'glibly' == j or
              'glitch' == j or
              'glitches' == j or
              'gloatingly' == j or
              'gloom' == j or
              'gloomy' == j or
              'glower' == j or
              'glum' == j or
              'glut' == j or
              'gnawing' == j or
              'goad' == j or
              'goading' == j or
              'god-awful' == j or
              'goof' == j or
              'goofy' == j or
              'goon' == j or
              'gossip' == j or
              'graceless' == j or
              'gracelessly' == j or
              'graft' == j or
              'grainy' == j or
              'grapple' == j or
              'grate' == j or
              'grating' == j or
              'gravely' == j or
              'greasy' == j or
              'greed' == j or
              'greedy' == j or
              'grief' == j or
              'grievance' == j or
              'grievances' == j or
              'grieve' == j or
              'grieving' == j or
              'grievous' == j or
              'grievously' == j or
              'grim' == j or
              'grimace' == j or
              'grind' == j or
              'gripe' == j or
              'gripes' == j or
              'grisly' == j or
              'gritty' == j or
              'gross' == j or
              'grossly' == j or
              'grotesque' == j or
              'grouch' == j or
              'grouchy' == j or
              'groundless' == j or
              'grouse' == j or
              'growl' == j or
              'grudge' == j or
              'grudges' == j or
              'grudging' == j or
              'grudgingly' == j or
              'gruesome' == j or
              'gruesomely' == j or
              'gruff' == j or
              'grumble' == j or
              'grumpier' == j or
              'grumpiest' == j or
              'grumpily' == j or
              'grumpy' == j or
              'guile' == j or
              'guilt' == j or
              'guiltily' == j or
              'guilty' == j or
              'gullible' == j or
              'gutless' == j or
              'fucked' == j):
            n += 1
    if (n > 0):
        print(Fore.RED+"your entered sentence seems to be negative".title())
        print(Style.RESET_ALL)
    elif (p > 0):
        print(Fore.GREEN+"your entered sentence seems to be positive".title())
        print(Style.RESET_ALL)
    else:
        print(Fore.BLUE+"your sentence seems too be neutral".title())
        print(Style.RESET_ALL)
        print(p, n)
