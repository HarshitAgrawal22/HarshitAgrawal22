
#====================file handling==============================#
with open("secfile.txt") as s:
    s=s.readlines()
#====================functions==============================#
def positive():
    c=0
    for i in range(len(s)):
        if ("good" in s[i] or
                "best" in s[i] or
                "better" in s[i] or
                "nice" in s[i] or
                "perfect" in s[i] or
                "hehe" in s[i] or
                "cheerful" in s[i] or
                'Adaptable' in s[i] or
                'Adventurous' in s[i] or
                'Amazing' in s[i] or
                'Amiable' in s[i] or
                'Beautiful' in s[i] or
                'Becoming' in s[i] or
                'Beloved' in s[i] or
                'Blessed' in s[i] or
                'Blissful' in s[i] or
                'Brotherly' in s[i] or
                'Calming' in s[i] or
                'Captivating' in s[i] or
                'Charming' in s[i] or
                'Cherished' in s[i] or
                'Comforting' in s[i] or
                'Compelling' in s[i] or
                'Considerable' in s[i] or
                'Credible' in s[i] or
                'Dapper' in s[i] or
                'Darling' in s[i] or
                'Delicious' in s[i] or
                'Delightful' in s[i] or
                'Dependable' in s[i] or
                'Desirable' in s[i] or
                'Dreamy' in s[i] or
                'Durable' in s[i] or
                'Elegant' in s[i] or
                'Empowering' in s[i] or
                'Enchanting' in s[i] or
                'Endearing' in s[i] or
                'Energising' in s[i] or
                'Enjoyable' in s[i] or
                'Enlightening' in s[i] or
                'Exceptional' in s[i] or
                'Fabulous' in s[i] or
                'Fancy' in s[i] or
                'Fantastic' in s[i] or
                'Fashionable' in s[i] or
                'Faultless' in s[i] or
                'Fetching' in s[i] or
                'Flourishing' in s[i] or
                'Formidable' in s[i] or
                'Fulfilling' in s[i] or
                'Funny' in s[i] or
                'Generous' in s[i] or
                'Gifted' in s[i] or
                'Glamorous' in s[i] or
                'Gleaming' in s[i] or
                'Glowing' in s[i] or
                'Godly' in s[i] or
                'Gracious' in s[i] or
                'Gratifying' in s[i] or
                'Happening' in s[i] or
                'Harmonious' in s[i] or
                'Heavenly' in s[i] or
                'Honourable' in s[i] or
                'Ideal' in s[i] or
                'Important' in s[i] or
                'Incredible' in s[i] or
                'Indispensable' in s[i] or
                'Indisputable' in s[i] or
                'Influential' in s[i] or
                'Inspiring' in s[i] or
                'Interesting' in s[i] or
                'Irresistible' in s[i] or
                'Joyful' in s[i] or
                'Jolly' in s[i] or
                'Jovial' in s[i] or
                'Kindly' in s[i] or
                'Kingly' in s[i] or
                'Leading' in s[i] or
                'Legendary' in s[i] or
                'Liberating' in s[i] or
                'Likeable' in s[i] or
                'Lordly' in s[i] or
                'Lovable' in s[i] or
                'Luscious' in s[i] or
                'Magical' in s[i] or
                'Majestic' in s[i] or
                'Memorable' in s[i] or
                'Mesmerizing' in s[i] or
                'Mighty' in s[i] or
                'Miraculous' in s[i] or
                'Motivational' in s[i] or
                'Nifty' in s[i] or
                'Obliging' in s[i] or
                'Optimal' in s[i] or
                'Original' in s[i] or

                'Palatable' in s[i] or
                'Paramount' in s[i] or
                'Peaceful' in s[i] or
                'Peachy' in s[i] or
                'Perfect' in s[i] or
                'Phenomenal' in s[i] or
                'Picturesque' in s[i] or
                'Pleasant' in s[i] or
                'Pleasing' in s[i] or
                'Pleasurable' in s[i] or
                'Positive' in s[i] or
                'Powerful' in s[i] or
                'Praiseworthy' in s[i] or
                'Precious' in s[i] or
                'Prestigious' in s[i] or
                'Prizewinning' in s[i] or
                'Promising' in s[i] or
                'Quality' in s[i] or
                'Radiant' in s[i] or
                'Reasonable' in s[i] or
                'Refreshing' in s[i] or
                'Reliable' in s[i] or
                'Respectable' in s[i] or
                'Revolutionary' in s[i] or
                'Rewarding' in s[i] or
                'Rousing' in s[i] or
                'Saintly' in s[i] or
                'Salubrious' in s[i] or
                'Satisfying' in s[i] or
                'Scrumptious' in s[i] or
                'Sensational' in s[i] or
                'Sexy' in s[i] or
                'Shiny' in s[i] or
                'Showy' in s[i] or
                'Smashing' in s[i] or
                'Soothing' in s[i] or
                'Sought-after' in s[i] or
                'Spectacular' in s[i] or
                'Spiffy' in s[i] or
                'Stimulating' in s[i] or
                'Striking' in s[i] or
                'Stunning' in s[i] or
                'Stupendous' in s[i] or
                'Superb' in s[i] or
                'Supreme' in s[i] or
                'Swanky' in s[i] or
                'Tasteful' in s[i] or
                'Tasty' in s[i] or
                'Terrific' in s[i] or
                'Thrilling' in s[i] or
                'Titillating' in s[i] or
                'Tremendous' in s[i] or
                'Trusty' in s[i] or
                'Ultimate' in s[i] or
                'Unbelievable' in s[i] or
                'Uplifting' in s[i] or
                'Useful' in s[i] or
                'Valuable' in s[i] or
                'Vibrant' in s[i]
        ):

            c+=1
            print(s[i],"\t\n it is a positive comment",c)
def negative():
    v=0
    for i in range(len(s)):
        if ("bad" in s[i] or
              "worse" in s[i] or
              "worst" in s[i] or
              "not good" in s[i] or
              "nor" in s[i] or
              "neither " in s[i] or
              "not " in s[i] or
              "no " in s[i] or
              "fuck" in s[i] or
              "fuckoff" in s[i] or
              'embarrass'
              'embarrassing'
              'abolish' in s[i] or
                'abominable' in s[i] or
                'abominably' in s[i] or
                'abominate' in s[i] or
                'abomination' in s[i] or
                'abort' in s[i] or
                'aborted' in s[i] or
                'aborts' in s[i] or
                'abrade' in s[i] or
                'abrasive' in s[i] or
                'abrupt' in s[i] or
                'abruptly' in s[i] or
                'abscond' in s[i] or
                'absence' in s[i] or
                'absent-minded' in s[i] or
                'absentee' in s[i] or
                'absurd' in s[i] or
                'absurdity' in s[i] or
                'absurdly' in s[i] or
                'absurdness' in s[i] or
                'abuse' in s[i] or
                'abused' in s[i] or
                'abuses' in s[i] or
                'abusive' in s[i] or
                'abysmal' in s[i] or
                'abysmally' in s[i] or
                'abyss' in s[i] or
                'accidental' in s[i] or
                'accost' in s[i] or
                'accursed' in s[i] or
                'accusation' in s[i] or
                'accusations' in s[i] or
                'accuse' in s[i] or
                'accuses' in s[i] or
                'accusing' in s[i] or
                'accusingly' in s[i] or
                'acerbate' in s[i] or
                'acerbic' in s[i] or
                'acerbically' in s[i] or
                'ache' in s[i] or
                'ached' in s[i] or
                'aches' in s[i] or
                'aching' in s[i] or
                'acrid' in s[i] or
                'acridly' in s[i] or
                'acridness' in s[i] or
                'acrimonious' in s[i] or
                'acrimoniously' in s[i] or
                'acrimony' in s[i] or
                'adamant' in s[i] or
                'adamantly' in s[i] or
                'addict' in s[i] or
                'addicted' in s[i] or
                'addicting' in s[i] or
                'addicts' in s[i] or
                'admonish' in s[i] or
                'admonisher' in s[i] or
                'admonishingly' in s[i] or
                'admonis…' in s[i] or
                'babble' in s[i] or
                'back-logged' in s[i] or
                'back-wood' in s[i] or
                'back-woods' in s[i] or
                'backache' in s[i] or
                'backaches' in s[i] or
                'backbite' in s[i] or
                'backbiting' in s[i] or
                'backward' in s[i] or
                'backwardness' in s[i] or
                'backwoods' in s[i] or
                'bad' in s[i] or
                'badly' in s[i] or
                'baffle' in s[i] or
                'baffled' in s[i] or
                'bafflement' in s[i] or
                'baffling' in s[i] or
                'bait' in s[i] or
                'balk' in s[i] or
                'banal' in s[i] or
                'bane' in s[i] or
                'banish' in s[i] or
                'banishment' in s[i] or
                'bankrupt' in s[i] or
                'barbarian' in s[i] or
                'barbaric' in s[i] or
                'barbarically' in s[i] or
                'barbarity' in s[i] or
                'barbarous' in s[i] or
                'barbarously' in s[i] or
                'barren' in s[i] or
                'baseless' in s[i] or
                'bash' in s[i] or
                'bashed' in s[i] or
                'bashful' in s[i] or
                'bashing' in s[i] or
                'battered' in s[i] or
                'battering' in s[i] or
                'batty' in s[i] or
                'bearish' in s[i] or
                'beastly' in s[i] or
                'bedlam' in s[i] or
                'bedlamite' in s[i] or
                'befoul' in s[i] or
                'beg' in s[i] or
                'beggar' in s[i] or
                'beggarly' in s[i] or
                'begging' in s[i] or
                'beguile' in s[i] or
                'belabor' in s[i] or
                'belated' in s[i] or
                'beleaguer' in s[i] or
                'belie' in s[i] or
                'belittle' in s[i] or
                'belittled' in s[i] or
                'belittling' in s[i] or
                'bellicose' in s[i] or
                'belligerence' in s[i] or
                'belligerent' in s[i] or
                'belligerently' in s[i] or
                '…' in s[i] or
                'cackle' in s[i] or
                'calamities' in s[i] or
                'calamitous' in s[i] or
                'calamitously' in s[i] or
                'calamity' in s[i] or
                'callous' in s[i] or
                'calumniate' in s[i] or
                'calumniation' in s[i] or
                'calumnies' in s[i] or
                'calumnious' in s[i] or
                'calumniously' in s[i] or
                'calumny' in s[i] or
                'cancer' in s[i] or
                'cancerous' in s[i] or
                'cannibal' in s[i] or
                'cannibalize' in s[i] or
                'capitulate' in s[i] or
                'capricious' in s[i] or
                'capriciously' in s[i] or
                'capriciousness' in s[i] or
                'capsize' in s[i] or
                'careless' in s[i] or
                'carelessness' in s[i] or
                'caricature' in s[i] or
                'carnage' in s[i] or
                'carp' in s[i] or
                'cartoonish' in s[i] or
                'cash-strapped' in s[i] or
                'castigate' in s[i] or
                'castrated' in s[i] or
                'casualty' in s[i] or
                'cataclysm' in s[i] or
                'cataclysmal' in s[i] or
                'cataclysmic' in s[i] or
                'cataclysmically' in s[i] or
                'catastrophe' in s[i] or
                'catastrophes' in s[i] or
                'catastrophic' in s[i] or
                'catastrophically' in s[i] or
                'caustic' in s[i] or
                'caustically' in s[i] or
                'cautionary' in s[i] or
                'cave' in s[i] or
                'censure' in s[i] or
                'chafe' in s[i] or
                'chaff' in s[i] or
                'chagrin' in s[i] or
                'challenging' in s[i] or
                'chaos' in s[i] or
                'chaotic' in s[i] or
                'chasten' in s[i] or
                'chastise' in s[i] or
                'chastisement' in s[i] or
                'chatte…' in s[i] or
                'damage' in s[i] or
                'damaged' in s[i] or
                'damages' in s[i] or
                'damaging' in s[i] or
                'damn' in s[i] or
                'damnable' in s[i] or
                'damnably' in s[i] or
                'damnation' in s[i] or
                'damned' in s[i] or
                'damning' in s[i] or
                'damper' in s[i] or
                'danger' in s[i] or
                'dangerous' in s[i] or
                'dangerousness' in s[i] or
                'dark' in s[i] or
                'darken' in s[i] or
                'darkened' in s[i] or
                'darker' in s[i] or
                'darkness' in s[i] or
                'dastard' in s[i] or
                'dastardly' in s[i] or
                'daunt' in s[i] or
                'daunting' in s[i] or
                'dauntingly' in s[i] or
                'dawdle' in s[i] or
                'daze' in s[i] or
                'dazed' in s[i] or
                'dead' in s[i] or
                'deadbeat' in s[i] or
                'deadlock' in s[i] or
                'deadly' in s[i] or
                'deadweight' in s[i] or
                'deaf' in s[i] or
                'dearth' in s[i] or
                'death' in s[i] or
                'debacle' in s[i] or
                'debase' in s[i] or
                'debasement' in s[i] or
                'debaser' in s[i] or
                'debatable' in s[i] or
                'debauch' in s[i] or
                'debaucher' in s[i] or
                'debauchery' in s[i] or
                'debilitate' in s[i] or
                'debilitating' in s[i] or
                'debility' in s[i] or
                'debt' in s[i] or
                'debts' in s[i] or
                'decadence' in s[i] or
                'decadent' in s[i] or
                'decay' in s[i] or
                'decayed' in s[i] or
                'deceit' in s[i] or
                'deceitful' in s[i] or
                'deceitfully' in s[i] or
                'deceitfulness' in s[i] or
                'deceive' in s[i] or
                'deceiver' in s[i] or
                'deceivers' in s[i] or
                'deceiving' in s[i] or
                'deception' in s[i] or
                'deceptiv…' in s[i] or
                'earsplitting' in s[i] or
                'eccentric' in s[i] or
                'eccentricity' in s[i] or
                'effigy' in s[i] or
                'effrontery' in s[i] or
                'egocentric' in s[i] or
                'egomania' in s[i] or
                'egotism' in s[i] or
                'egotistical' in s[i] or
                'egotistically' in s[i] or
                'egregious' in s[i] or
                'egregiously' in s[i] or
                'election-rigger' in s[i] or
                'elimination' in s[i] or
                'emaciated' in s[i] or
                'emasculate' in s[i] or
                'embarrass' in s[i] or
                'embarrassing' in s[i] or
                'embarrassingly' in s[i] or
                'embarrassment' in s[i] or
                'embattled' in s[i] or
                'embroil' in s[i] or
                'embroiled' in s[i] or
                'embroilment' in s[i] or
                'emergency' in s[i] or
                'emphatic' in s[i] or
                'emphatically' in s[i] or
                'emptiness' in s[i] or
                'encroach' in s[i] or
                'encroachment' in s[i] or
                'endanger' in s[i] or
                'enemies' in s[i] or
                'enemy' in s[i] or
                'enervate' in s[i] or
                'enfeeble' in s[i] or
                'enflame' in s[i] or
                'engulf' in s[i] or
                'enjoin' in s[i] or
                'enmity' in s[i] or
                'enrage' in s[i] or
                'enraged' in s[i] or
                'enraging' in s[i] or
                'enslave' in s[i] or
                'entangle' in s[i] or
                'entanglement' in s[i] or
                'entrap' in s[i] or
                'entrapment' in s[i] or
                'envious' in s[i] or
                'enviously' in s[i] or
                'enviousness' in s[i] or
                'epidemic' in s[i] or
                'equivocal' in s[i] or
                'erase' in s[i] or
                'erode' in s[i] or
                'erodes' in s[i] or
                'ero…' in s[i] or
                'f ** k' in s[i] or
                'fabricate' in s[i] or
                'fabrication' in s[i] or
                'facetious' in s[i] or
                'facetiously' in s[i] or
                'fail' in s[i] or
                'failed' in s[i] or
                'failing' in s[i] or
                'fails' in s[i] or
                'failure' in s[i] or
                'failures' in s[i] or
                'faint' in s[i] or
                'fainthearted' in s[i] or
                'faithless' in s[i] or
                'fake' in s[i] or
                'fall' in s[i] or
                'fallacies' in s[i] or
                'fallacious' in s[i] or
                'fallaciously' in s[i] or
                'fallaciousness' in s[i] or
                'fallacy' in s[i] or
                'fallen' in s[i] or
                'falling' in s[i] or
                'fallout' in s[i] or
                'falls' in s[i] or
                'FALSE' in s[i] or
                'falsehood' in s[i] or
                'falsely' in s[i] or
                'falsify' in s[i] or
                'falter' in s[i] or
                'faltered' in s[i] or
                'famine' in s[i] or
                'famished' in s[i] or
                'fanatic' in s[i] or
                'fanatical' in s[i] or
                'fanatically' in s[i] or
                'fanaticism' in s[i] or
                'fanatics' in s[i] or
                'fanciful' in s[i] or
                'far-fetched' in s[i] or
                'farce' in s[i] or
                'farcical' in s[i] or
                'farcical-yet-provocative' in s[i] or
                'farcically' in s[i] or
                'farfetched' in s[i] or
                'fascism' in s[i] or
                'fascist' in s[i] or
                'fastidious' in s[i] or
                'fastidiously' in s[i] or
                'fat' in s[i] or
                'fat-cat' in s[i] or
                'fat-cats' in s[i] or
                'fatal' in s[i] or
                'fatalistic' in s[i] or
                'fatalistically' in s[i] or
                'fatally' in s[i] or
                'fateful' in s[i] or
                'fatefully' in s[i] or
                'fat…' in s[i] or
                'gabble' in s[i] or
                'gaff' in s[i] or
                'gaffe' in s[i] or
                'gainsay' in s[i] or
                'gainsayer' in s[i] or
                'gall' in s[i] or
                'galling' in s[i] or
                'gallingly' in s[i] or
                'galls' in s[i] or
                'gangster' in s[i] or
                'gape' in s[i] or
                'garbage' in s[i] or
                'garish' in s[i] or
                'gasp' in s[i] or
                'gauche' in s[i] or
                'gaudy' in s[i] or
                'gawk' in s[i] or
                'gawky' in s[i] or
                'geezer' in s[i] or
                'genocide' in s[i] or
                'get-rich' in s[i] or
                'ghastly' in s[i] or
                'ghetto' in s[i] or
                'ghosting' in s[i] or
                'gibber' in s[i] or
                'gibberish' in s[i] or
                'gibe' in s[i] or
                'giddy' in s[i] or
                'gimmick' in s[i] or
                'gimmicked' in s[i] or
                'gimmicking' in s[i] or
                'gimmicks' in s[i] or
                'gimmicky' in s[i] or
                'glare' in s[i] or
                'glaringly' in s[i] or
                'glib' in s[i] or
                'glibly' in s[i] or
                'glitch' in s[i] or
                'glitches' in s[i] or
                'gloatingly' in s[i] or
                'gloom' in s[i] or
                'gloomy' in s[i] or
                'glower' in s[i] or
                'glum' in s[i] or
                'glut' in s[i] or
                'gnawing' in s[i] or
                'goad' in s[i] or
                'goading' in s[i] or
                'god-awful' in s[i] or
                'goof' in s[i] or
                'goofy' in s[i] or
                'goon' in s[i] or
                'gossip' in s[i] or
                'graceless' in s[i] or
                'gracelessly' in s[i] or
                'graft' in s[i] or
                'grainy' in s[i] or
                'grapple' in s[i] or
                'grate' in s[i] or
                'grating' in s[i] or
                'gravely' in s[i] or
                'greasy' in s[i] or
                'greed' in s[i] or
                'greedy' in s[i] or
                'grief' in s[i] or
                'grievance' in s[i] or
                'grievances' in s[i] or
                'gr…' in s[i] or
                'hack' in s[i] or
                'hacks' in s[i] or
                'haggard' in s[i] or
                'haggle' in s[i] or
                'halfhearted' in s[i] or
                'halfheartedly' in s[i] or
                'hallucinate' in s[i] or
                'hallucination' in s[i] or
                'hamper' in s[i] or
                'hampered' in s[i] or
                'handicapped' in s[i] or
                'hang' in s[i] or
                'hangs' in s[i] or
                'haphazard' in s[i] or
                'hapless' in s[i] or
                'harangue' in s[i] or
                'harass' in s[i] or
                'harassed' in s[i] or
                'harasses' in s[i] or
                'harassment' in s[i] or
                'harboring' in s[i] or
                'harbors' in s[i] or
                'hard' in s[i] or
                'hard-hit' in s[i] or
                'hard-liner' in s[i] or
                'hardball' in s[i] or
                'harden' in s[i] or
                'hardened' in s[i] or
                'hardheaded' in s[i] or
                'hardhearted' in s[i] or
                'hardliner' in s[i] or
                'hardliners' in s[i] or
                'hardship' in s[i] or
                'hardships' in s[i] or
                'harm' in s[i] or
                'harmed' in s[i] or
                'harmful' in s[i] or
                'harms' in s[i] or
                'harpy' in s[i] or
                'harridan' in s[i] or
                'harried' in s[i] or
                'harrow' in s[i] or
                'harsh' in s[i] or
                'harshly' in s[i] or
                'hassle' in s[i] or
                'hassled' in s[i] or
                'hassles' in s[i] or
                'haste' in s[i] or
                'hastily' in s[i] or
                'hasty' in s[i] or
                'hate' in s[i] or
                'hated' in s[i] or
                'hateful' in s[i] or
                'hatefully' in s[i] or
                'hatefulness' in s[i] or
                'hater' in s[i] or
                'haters' in s[i] or
                'hates' in s[i] or
                'hating' in s[i] or
                'hatred' in s[i] or
                'haughtily' in s[i] or
                'haughty' in s[i] or
                'haun…' in s[i] or
                'idiocies' in s[i] or
                'idiocy' in s[i] or
                'idiot' in s[i] or
                'idiotic' in s[i] or
                'idiotically' in s[i] or
                'idiots' in s[i] or
                'idle' in s[i] or
                'ignoble' in s[i] or
                'ignominious' in s[i] or
                'ignominiously' in s[i] or
                'ignominy' in s[i] or
                'ignorance' in s[i] or
                'ignorant' in s[i] or
                'ignore' in s[i] or
                'ill-advised' in s[i] or
                'ill-conceived' in s[i] or
                'ill-defined' in s[i] or
                'ill-designed' in s[i] or
                'ill-fated' in s[i] or
                'ill-favored' in s[i] or
                'ill-formed' in s[i] or
                'ill-mannered' in s[i] or
                'ill-natured' in s[i] or
                'ill-sorted' in s[i] or
                'ill-tempered' in s[i] or
                'ill-treated' in s[i] or
                'ill-treatment' in s[i] or
                'ill-usage' in s[i] or
                'ill-used' in s[i] or
                'illegal' in s[i] or
                'illegally' in s[i] or
                'illegitimate' in s[i] or
                'illicit' in s[i] or
                'illiterate' in s[i] or
                'illness' in s[i] or
                'illogical' in s[i] or
                'illogically' in s[i] or
                'illusion' in s[i] or
                'illusions' in s[i] or
                'illusory' in s[i] or
                'imaginary' in s[i] or
                'imbalance' in s[i] or
                'imbecile' in s[i] or
                'imbroglio' in s[i] or
                'immaterial' in s[i] or
                'immature' in s[i] or
                'imminence' in s[i] or
                'imminently' in s[i] or
                'immobilized' in s[i] or
                'immoderate' in s[i] or
                'immoderately' in s[i] or
                'immodest' in s[i] or
                'immoral' in s[i] or
                'immorality' in s[i] or
                'jabber' in s[i] or
                'jaded' in s[i] or
                'jagged' in s[i] or
                'jam' in s[i] or
                'jarring' in s[i] or
                'jaundiced' in s[i] or
                'jealous' in s[i] or
                'jealously' in s[i] or
                'jealousness' in s[i] or
                'jealousy' in s[i] or
                'jeer' in s[i] or
                'jeering' in s[i] or
                'jeeringly' in s[i] or
                'jeers' in s[i] or
                'jeopardize' in s[i] or
                'jeopardy' in s[i] or
                'jerk' in s[i] or
                'jerky' in s[i] or
                'jitter' in s[i] or
                'jitters' in s[i] or
                'jittery' in s[i] or
                'job-killing' in s[i] or
                'jobless' in s[i] or
                'joke' in s[i] or
                'joker' in s[i] or
                'jolt' in s[i] or
                'judder' in s[i] or
                'juddering' in s[i] or
                'judders' in s[i] or
                'jumpy' in s[i] or
                'junk' in s[i] or
                'junky' in s[i] or
                'junkyard' in s[i] or
                'kill' in s[i] or
                'killed' in s[i] or
                'killer' in s[i] or
                'killing' in s[i] or
                'killjoy' in s[i] or
                'kills' in s[i] or
                'knave' in s[i] or
                'knife' in s[i] or
                'knock' in s[i] or
                'knotted' in s[i] or
                'kook' in s[i] or
                'kooky' in s[i] or
                'lack' in s[i] or
                'lackadaisical' in s[i] or
                'lacked' in s[i] or
                'lackey' in s[i] or
                'lackeys' in s[i] or
                'lacking' in s[i] or
                'lackluster' in s[i] or
                'lacks' in s[i] or
                'laconic' in s[i] or
                'lag' in s[i] or
                'lagged' in s[i] or
                'lagging' in s[i] or
                'lags' in s[i] or
                'laid-off' in s[i] or
                'lambast' in s[i] or
                'lambaste' in s[i] or
                'lame' in s[i] or
                'lame-duck' in s[i] or
                'lament' in s[i] or
                'lamentable' in s[i] or
                'lamentably' in s[i] or
                'languid' in s[i] or
                'languish' in s[i] or
                'languor' in s[i] or
                'languorous' in s[i] or
                'languorously' in s[i] or
                'lanky' in s[i] or
                'lapse' in s[i] or
                'lapsed' in s[i] or
                'lapses' in s[i] or
                'lascivious' in s[i] or
                'last-ditch' in s[i] or
                'latency' in s[i] or
                'laughable' in s[i] or
                'laughably' in s[i] or
                'laughingstock' in s[i] or
                'lawbreaker' in s[i] or
                'lawbreaking' in s[i] or
                'lawless' in s[i] or
                'lawlessness' in s[i] or
                'layoff' in s[i] or
                'layoff-happy' in s[i] or
                'lazy' in s[i] or
                'leak' in s[i] or
                'leakage' in s[i] or
                'leakages' in s[i] or
                'leaking' in s[i] or
                'leaks' in s[i] or
                'leaky' in s[i] or
                'lecher' in s[i] or
                'lecherous' in s[i] or
                'lechery' in s[i] or
                'leech' in s[i] or
                'leer' in s[i] or
                'leery' in s[i] or
                'left-leaning' in s[i] or
                'lemon' in s[i] or
                'lengthy' in s[i] or
                'less-developed' in s[i] or
                'lesser-known' in s[i] or
                'letch' in s[i] or
                'leth…' in s[i] or
                'macabre' in s[i] or
                'mad' in s[i] or
                'madden' in s[i] or
                'maddening' in s[i] or
                'maddeningly' in s[i] or
                'madder' in s[i] or
                'madly' in s[i] or
                'madman' in s[i] or
                'madness' in s[i] or
                'maladjusted' in s[i] or
                'maladjustment' in s[i] or
                'malady' in s[i] or
                'malaise' in s[i] or
                'malcontent' in s[i] or
                'malcontented' in s[i] or
                'maledict' in s[i] or
                'malevolence' in s[i] or
                'malevolent' in s[i] or
                'malevolently' in s[i] or
                'malice' in s[i] or
                'malicious' in s[i] or
                'maliciously' in s[i] or
                'maliciousness' in s[i] or
                'malign' in s[i] or
                'malignant' in s[i] or
                'malodorous' in s[i] or
                'maltreatment' in s[i] or
                'mangle' in s[i] or
                'mangled' in s[i] or
                'mangles' in s[i] or
                'mangling' in s[i] or
                'mania' in s[i] or
                'maniac' in s[i] or
                'maniacal' in s[i] or
                'manic' in s[i] or
                'manipulate' in s[i] or
                'manipulation' in s[i] or
                'manipulative' in s[i] or
                'manipulators' in s[i] or
                'mar' in s[i] or
                'marginal' in s[i] or
                'marginally' in s[i] or
                'martyrdom' in s[i] or
                'martyrdom-seeking' in s[i] or
                'mashed' in s[i] or
                'massacre' in s[i] or
                'massacres' in s[i] or
                'matte' in s[i] or
                'mawkish' in s[i] or
                'mawkishly' in s[i] or
                'mawkishness' in s[i] or
                'meager' in s[i] or
                'meaningless' in s[i] or
                'meanness' in s[i] or
                'measly' in s[i] or
                'meddle' in s[i] or
                'meddlesome' in s[i] or
                'nag' in s[i] or
                'nagging' in s[i] or
                'naive' in s[i] or
                'naively' in s[i] or
                'narrower' in s[i] or
                'nastily' in s[i] or
                'nastiness' in s[i] or
                'nasty' in s[i] or
                'naughty' in s[i] or
                'nauseate' in s[i] or
                'nauseates' in s[i] or
                'nauseating' in s[i] or
                'nauseatingly' in s[i] or
                'naïve' in s[i] or
                'nebulous' in s[i] or
                'nebulously' in s[i] or
                'needless' in s[i] or
                'needlessly' in s[i] or
                'needy' in s[i] or
                'nefarious' in s[i] or
                'nefariously' in s[i] or
                'negate' in s[i] or
                'negation' in s[i] or
                'negative' in s[i] or
                'negatives' in s[i] or
                'negativity' in s[i] or
                'neglect' in s[i] or
                'neglected' in s[i] or
                'negligence' in s[i] or
                'negligent' in s[i] or
                'nemesis' in s[i] or
                'nepotism' in s[i] or
                'nervous' in s[i] or
                'nervously' in s[i] or
                'nervousness' in s[i] or
                'nettle' in s[i] or
                'nettlesome' in s[i] or
                'neurotic' in s[i] or
                'neurotically' in s[i] or
                'niggle' in s[i] or
                'niggles' in s[i] or
                'nightmare' in s[i] or
                'nightmarish' in s[i] or
                'nightmarishly' in s[i] or
                'nitpick' in s[i] or
                'nitpicking' in s[i] or
                'noise' in s[i] or
                'noises' in s[i] or
                'noisier' in s[i] or
                'noisy' in s[i] or
                'non-confidence' in s[i] or
                'nonexistent' in s[i] or
                'nonresponsive' in s[i] or
                'nonsense' in s[i] or
                'nosey' in s[i] or
                'notoriety' in s[i] or
                'notorious' in s[i] or
                'notoriously' in s[i] or
                'noxious' in s[i] or
                'nuisance' in s[i] or
                'numb' in s[i] or
                'obese' in s[i] or
                'object' in s[i] or
                'objection' in s[i] or
                'objectionable' in s[i] or
                'objections' in s[i] or
                'oblique' in s[i] or
                'obliterate' in s[i] or
                'obliterated' in s[i] or
                'oblivious' in s[i] or
                'obnoxious' in s[i] or
                'obnoxiously' in s[i] or
                'obscene' in s[i] or
                'obscenely' in s[i] or
                'obscenity' in s[i] or
                'obscure' in s[i] or
                'obscured' in s[i] or
                'obscures' in s[i] or
                'obscurity' in s[i] or
                'obsess' in s[i] or
                'obsessive' in s[i] or
                'obsessively' in s[i] or
                'obsessiveness' in s[i] or
                'obsolete' in s[i] or
                'obstacle' in s[i] or
                'obstinate' in s[i] or
                'obstinately' in s[i] or
                'obstruct' in s[i] or
                'obstructed' in s[i] or
                'obstructing' in s[i] or
                'obstruction' in s[i] or
                'obstructs' in s[i] or
                'obtrusive' in s[i] or
                'obtuse' in s[i] or
                'occlude' in s[i] or
                'occluded' in s[i] or
                'occludes' in s[i] or
                'occluding' in s[i] or
                'odd' in s[i] or
                'odder' in s[i] or
                'oddest' in s[i] or
                'oddities' in s[i] or
                'oddity' in s[i] or
                'oddly' in s[i] or
                'odor' in s[i] or
                'offence' in s[i] or
                'offend' in s[i] or
                'offender' in s[i] or
                'offending' in s[i] or
                'offenses' in s[i] or
                'offensive' in s[i] or
                'offensively' in s[i] or
                'offensiveness' in s[i] or
                'officious' in s[i] or
                'ominous' in s[i] or
                'ominously' in s[i] or
                'omission' in s[i] or
                'omit' in s[i] or
                'one-sided' in s[i] or
                'pain' in s[i] or
                'painful' in s[i] or
                'painfully' in s[i] or
                'pains' in s[i] or
                'pale' in s[i] or
                'pales' in s[i] or
                'paltry' in s[i] or
                'pan' in s[i] or
                'pandemonium' in s[i] or
                'pander' in s[i] or
                'pandering' in s[i] or
                'panders' in s[i] or
                'panic' in s[i] or
                'panicked' in s[i] or
                'panicking' in s[i] or
                'panicky' in s[i] or
                'paradoxical' in s[i] or
                'paradoxically' in s[i] or
                'paralyzed' in s[i] or
                'paranoia' in s[i] or
                'paranoid' in s[i] or
                'parasite' in s[i] or
                'pariah' in s[i] or
                'parody' in s[i] or
                'partiality' in s[i] or
                'partisan' in s[i] or
                'partisans' in s[i] or
                'passive' in s[i] or
                'passiveness' in s[i] or
                'pathetic' in s[i] or
                'pathetically' in s[i] or
                'patronize' in s[i] or
                'paucity' in s[i] or
                'pauper' in s[i] or
                'paupers' in s[i] or
                'payback' in s[i] or
                'peculiar' in s[i] or
                'peculiarly' in s[i] or
                'pedantic' in s[i] or
                'peeled' in s[i] or
                'peeve' in s[i] or
                'peeved' in s[i] or
                'peevish' in s[i] or
                'peevishly' in s[i] or
                'penalize' in s[i] or
                'penalty' in s[i] or
                'perfidious' in s[i] or
                'perfunctory' in s[i] or
                'peril' in s[i] or
                'perilous' in s[i] or
                'perilously' in s[i] or
                'perish' in s[i] or
                'pernicious' in s[i] or
                'perplex' in s[i] or
                'perplexed' in s[i] or
                'perplexing' in s[i] or
                'perplexity' in s[i] or
                'persecute' in s[i] or
                'persecution' in s[i] or
                'quack' in s[i] or
                'qualm' in s[i] or
                'qualms' in s[i] or
                'quandary' in s[i] or
                'quarrel' in s[i] or
                'quarrels' in s[i] or
                'quarrelsome' in s[i] or
                'quash' in s[i] or
                'queer' in s[i] or
                'questionable' in s[i] or
                'quibble' in s[i] or
                'quibbles' in s[i] or
                'quitter' in s[i] or
                'rabid' in s[i] or
                'racism' in s[i] or
                'racist' in s[i] or
                'racists' in s[i] or
                'racy' in s[i] or
                'radical' in s[i] or
                'radicalization' in s[i] or
                'radically' in s[i] or
                'radicals' in s[i] or
                'rage' in s[i] or
                'ragged' in s[i] or
                'raging' in s[i] or
                'rail' in s[i] or
                'raked' in s[i] or
                'rampage' in s[i] or
                'rampant' in s[i] or
                'ramshackle' in s[i] or
                'rancor' in s[i] or
                'randomly' in s[i] or
                'rankle' in s[i] or
                'rant' in s[i] or
                'ranted' in s[i] or
                'ranting' in s[i] or
                'rants' in s[i] or
                'rape' in s[i] or
                'raped' in s[i] or
                'raping' in s[i] or
                'rascal' in s[i] or
                'rascals' in s[i] or
                'rash' in s[i] or
                'rattle' in s[i] or
                'rattled' in s[i] or
                'rattles' in s[i] or
                'ravage' in s[i] or
                'raving' in s[i] or
                'reactionary' in s[i] or
                'rebellious' in s[i] or
                'rebuff' in s[i] or
                'rebuke' in s[i] or
                'recalcitrant' in s[i] or
                'recant' in s[i] or
                'recession' in s[i] or
                'recessionary' in s[i] or
                'reckless' in s[i] or
                'recklessly' in s[i] or
                'recklessness' in s[i] or
                'recoil' in s[i] or
                'recourses' in s[i] or
                'redundancy' in s[i] or
                'redundant' in s[i] or
                'refusal' in s[i] or
                'refuse' in s[i] or
                'refused' in s[i] or
                'refuses' in s[i] or
                'refusing' in s[i] or
                'refutation' in s[i] or
                'refute' in s[i] or
                'refuted' in s[i] or
                'refutes' in s[i] or
                'refuting' in s[i] or
                'regress' in s[i] or
                'regression' in s[i] or
                'regressive' in s[i] or
                'sabotage' in s[i] or
                'sack' in s[i] or
                'sacrificed' in s[i] or
                'sad' in s[i] or
                'sadden' in s[i] or
                'sadly' in s[i] or
                'sadness' in s[i] or
                'sag' in s[i] or
                'sagged' in s[i] or
                'sagging' in s[i] or
                'saggy' in s[i] or
                'sags' in s[i] or
                'salacious' in s[i] or
                'sanctimonious' in s[i] or
                'sap' in s[i] or
                'sarcasm' in s[i] or
                'sarcastic' in s[i] or
                'sarcastically' in s[i] or
                'sardonic' in s[i] or
                'sardonically' in s[i] or
                'sass' in s[i] or
                'satirical' in s[i] or
                'satirize' in s[i] or
                'savage' in s[i] or
                'savaged' in s[i] or
                'savagery' in s[i] or
                'savages' in s[i] or
                'scaly' in s[i] or
                'scam' in s[i] or
                'scams' in s[i] or
                'scandal' in s[i] or
                'scandalize' in s[i] or
                'scandalized' in s[i] or
                'scandalous' in s[i] or
                'scandalously' in s[i] or
                'scandals' in s[i] or
                'scant' in s[i] or
                'scapegoat' in s[i] or
                'scar' in s[i] or
                'scarce' in s[i] or
                'scarcely' in s[i] or
                'scarcity' in s[i] or
                'scare' in s[i] or
                'scared' in s[i] or
                'scarier' in s[i] or
                'scariest' in s[i] or
                'scarily' in s[i] or
                'scarred' in s[i] or
                'scars' in s[i] or
                'scary' in s[i] or
                'scathing' in s[i] or
                'scathingly' in s[i] or
                'scoff' in s[i] or
                'scold' in s[i] or
                'scolded' in s[i] or
                'scolding' in s[i] or
                'scorching' in s[i] or
                'scorn' in s[i] or
                'scornful' in s[i] or
                'scornfully' in s[i] or
                'scoundrel' in s[i] or
                'scourge' in s[i] or
                'scowl' in s[i] or
                'taboo' in s[i] or
                'tacky' in s[i] or
                'taint' in s[i] or
                'tainted' in s[i] or
                'tamper' in s[i] or
                'tangle' in s[i] or
                'tangled' in s[i] or
                'tangles' in s[i] or
                'tank' in s[i] or
                'tanked' in s[i] or
                'tanks' in s[i] or
                'tantrum' in s[i] or
                'tardy' in s[i] or
                'tarnish' in s[i] or
                'tarnished' in s[i] or
                'tarnishes' in s[i] or
                'tarnishing' in s[i] or
                'tattered' in s[i] or
                'taunt' in s[i] or
                'taunting' in s[i] or
                'tauntingly' in s[i] or
                'taunts' in s[i] or
                'taut' in s[i] or
                'tawdry' in s[i] or
                'taxing' in s[i] or
                'tease' in s[i] or
                'teasingly' in s[i] or
                'tedious' in s[i] or
                'tediously' in s[i] or
                'temerity' in s[i] or
                'temper' in s[i] or
                'tempest' in s[i] or
                'temptation' in s[i] or
                'tenderness' in s[i] or
                'tense' in s[i] or
                'tension' in s[i] or
                'tentative' in s[i] or
                'tentatively' in s[i] or
                'tenuous' in s[i] or
                'tenuously' in s[i] or
                'tepid' in s[i] or
                'terrible' in s[i] or
                'terribleness' in s[i] or
                'terribly' in s[i] or
                'terror' in s[i] or
                'terror-genic' in s[i] or
                'terrorism' in s[i] or
                'terrorize' in s[i] or
                'testily' in s[i] or
                'testy' in s[i] or
                'tetchily' in s[i] or
                'tetchy' in s[i] or
                'thankless' in s[i] or
                'thicker' in s[i] or
                'thirst' in s[i] or
                'thorny' in s[i] or
                'thoughtless' in s[i] or
                'thoughtlessly' in s[i] or
                'thoughtlessness' in s[i] or
                'thrash' in s[i] or
                'threat' in s[i] or
                'threate…' in s[i] or
                'ugh' in s[i] or
                'uglier' in s[i] or
                'ugliest' in s[i] or
                'ugliness' in s[i] or
                'ugly' in s[i] or
                'ulterior' in s[i] or
                'ultimatum' in s[i] or
                'ultimatums' in s[i] or
                'ultra-hardline' in s[i] or
                'un-viewable' in s[i] or
                'unable' in s[i] or
                'unacceptable' in s[i] or
                'unacceptably' in s[i] or
                'unaccustomed' in s[i] or
                'unachievable' in s[i] or
                'unaffordable' in s[i] or
                'unappealing' in s[i] or
                'unattractive' in s[i] or
                'unauthentic' in s[i] or
                'unavailable' in s[i] or
                'unavoidably' in s[i] or
                'unbearable' in s[i] or
                'unbelievable' in s[i] or
                'unbelievably' in s[i] or
                'uncaring' in s[i] or
                'uncertain' in s[i] or
                'uncivil' in s[i] or
                'uncivilized' in s[i] or
                'unclean' in s[i] or
                'unclear' in s[i] or
                'uncollectible' in s[i] or
                'uncomfortable' in s[i] or
                'uncomfortably' in s[i] or
                'uncompetitive' in s[i] or
                'uncompromising' in s[i] or
                'uncompromisingly' in s[i] or
                'unconfirmed' in s[i] or
                'unconstitutional' in s[i] or
                'uncontrolled' in s[i] or
                'unconvincing' in s[i] or
                'unconvincingly' in s[i] or
                'uncooperative' in s[i] or
                'uncouth' in s[i] or
                'uncreative' in s[i] or
                'undecided' in s[i] or
                'undefined' in s[i] or
                'undependability' in s[i] or
                'undependable' in s[i] or
                'undercut' in s[i] or
                'u…' in s[i] or
                'vagrant' in s[i] or
                'vague' in s[i] or
                'vagueness' in s[i] or
                'vain' in s[i] or
                'vainly' in s[i] or
                'vanity' in s[i] or
                'vehement' in s[i] or
                'vehemently' in s[i] or
                'vengeance' in s[i] or
                'vengeful' in s[i] or
                'vengefully' in s[i] or
                'vengefulness' in s[i] or
                'venom' in s[i] or
                'venomous' in s[i] or
                'venomously' in s[i] or
                'vent' in s[i] or
                'vestiges' in s[i] or
                'vex' in s[i] or
                'vexation' in s[i] or
                'vexing' in s[i] or
                'vexingly' in s[i] or
                'vibrate' in s[i] or
                'vibrated' in s[i] or
                'vibrates' in s[i] or
                'vibrating' in s[i] or
                'vibration' in s[i] or
                'vice' in s[i] or
                'vicious' in s[i] or
                'viciously' in s[i] or
                'viciousness' in s[i] or
                'victimize' in s[i] or
                'vile' in s[i] or
                'vileness' in s[i] or
                'vilify' in s[i] or
                'villainous' in s[i] or
                'villainously' in s[i] or
                'villains' in s[i] or
                'vindictive' in s[i] or
                'vindictively' in s[i] or
                'vindictiveness' in s[i] or
                'violate' in s[i] or
                'violation' in s[i] or
                'violator' in s[i] or
                'violators' in s[i] or
                'violent' in s[i] or
                'violently' in s[i] or
                'viper' in s[i] or
                'virulence' in s[i] or
                'virulent' in s[i] or
                'virulently' in s[i] or
                'virus' in s[i] or
                'vociferous' in s[i] or
                'vociferously' in s[i] or
                'volatile' in s[i] or
                'volatility' in s[i] or
                'vomit' in s[i] or
                'vomited' in s[i] or
                'vomiting' in s[i] or
                'vomits' in s[i] or
                'vulgar' in s[i] or
                'vulnerable' in s[i] or
                'wail' in s[i] or
                'wallow' in s[i] or
                'wane' in s[i] or
                'waning' in s[i] or
                'wanton' in s[i] or
                'war-like' in s[i] or
                'warily' in s[i] or
                'wariness' in s[i] or
                'warlike' in s[i] or
                'warned' in s[i] or
                'warning' in s[i] or
                'warp' in s[i] or
                'warped' in s[i] or
                'wary' in s[i] or
                'washed-out' in s[i] or
                'waste' in s[i] or
                'wasted' in s[i] or
                'wasteful' in s[i] or
                'wastefulness' in s[i] or
                'wasting' in s[i] or
                'water-down' in s[i] or
                'watered-down' in s[i] or
                'wayward' in s[i] or
                'weak' in s[i] or
                'weaken' in s[i] or
                'weakening' in s[i] or
                'weaker' in s[i] or
                'weakness' in s[i] or
                'weaknesses' in s[i] or
                'weariness' in s[i] or
                'wearisome' in s[i] or
                'weary' in s[i] or
                'wedge' in s[i] or
                'weed' in s[i] or
                'weep' in s[i] or
                'weird' in s[i] or
                'weirdly' in s[i] or
                'wheedle' in s[i] or
                'whimper' in s[i] or
                'whine' in s[i] or
                'whining' in s[i] or
                'whiny' in s[i] or
                'whips' in s[i] or
                'wicked' in s[i] or
                'wickedly' in s[i] or
                'wickedness' in s[i] or
                'wild' in s[i] or
                'wildly' in s[i] or
                'wiles' in s[i] or
                'wilt' in s[i] or
                'wily' in s[i] or
                'wimpy' in s[i] or
                'wince' in s[i] or
                'wobble' in s[i] or
                'wobbled' in s[i] or
                'wobbles' in s[i] or
                'woe' in s[i] or
                'woebegone' in s[i] or
                'woeful' in s[i] or
                'woefully' in s[i] or
                'womanizer' in s[i] or
                'womanizing' in s[i] or
                'worn' in s[i] or
                'worried' in s[i] or
                'worriedly' in s[i] or
                'worrier' in s[i] or
                'worries' in s[i] or
                'worrisome' in s[i] or
                'worry' in s[i] or
                'worrying' in s[i] or
                'worryingly' in s[i] or
                'worse' in s[i] or
                'worsen' in s[i] or
                'worsening' in s[i] or
                'worst' in s[i] or
                'worthless' in s[i] or
                'worthlessly' in s[i] or
                'worthlessness' in s[i] or
                'wound' in s[i] or
                'wounds' in s[i] or
                'wrangle' in s[i] or
                'wrath' in s[i] or
                'wreak' in s[i] or
                'wreaked' in s[i] or
                'wreaks' in s[i] or
                'wreck' in s[i] or
                'wrest' in s[i] or
                'wrestle' in s[i] or
                'wretch' in s[i] or
                'wretched' in s[i] or
                'wretchedly' in s[i] or
                'wretchedness' in s[i] or
                'wrinkle' in s[i] or
                'wrinkled' in s[i] or
                'wrinkles' in s[i] or
                'writhe' in s[i] or
                'wrong' in s[i] or
                'wrongful' in s[i] or
                'wrongly' in s[i] or
                'wrought'in s[i]
              ):
             print(s[i], "\t\n this is a negative comment")
             v+=1
    print(f"there are total of {v} negative comments")
def neutral():
    g=0
    for i in range(len(s)):
        if("bad" in s[i] or
              "worse" in s[i] or
              "worst" in s[i] or
              "not good" in s[i] or
              "nor" in s[i] or
              "neither " in s[i] or
              "not " in s[i] or
              "no " in s[i] or
              "fuck" in s[i] or
              "fuckoff" in s[i] or
              'embarrass' not in s[i] or
              'embarrassing' not in s[i] or
              'abolish' not in s[i] or
            'abominable' not in s[i] or
                'abominably' not in s[i] or
                'abominate' not in s[i] or
                'abomination' not in s[i] or
                'abort' not in s[i] or
                'aborted' not in s[i] or
                'aborts' not in s[i] or
                'abrade' not in s[i] or
                'abrasive' not in s[i] or
                'abrupt' not in s[i] or
                'abruptly' not in s[i] or
                'abscond' not in s[i] or
                'absence' not in s[i] or
                'absent-minded' not in s[i] or
                'absentee' not in s[i] or
                'absurd' not in s[i] or
                'absurdity' not in s[i] or
                'absurdly' not in s[i] or
                'absurdness' not in s[i] or
                'abuse' not in s[i] or
                'abused' not in s[i] or
                'abuses' not in s[i] or
                'abusive' not in s[i] or
                'abysmal' not in s[i] or
                'abysmally' not in s[i] or
                'abyss' not in s[i] or
                'accidental' not in s[i] or
                'accost' not in s[i] or
                'accursed' not in s[i] or
                'accusation' not in s[i] or
                'accusations' not in s[i] or
                'accuse' not in s[i] or
                'accuses' not in s[i] or
                'accusing' not in s[i] or
                'accusingly' not in s[i] or
                'acerbate' not in s[i] or
                'acerbic' not in s[i] or
                'acerbically' not in s[i] or
                'ache' not in s[i] or
                'ached' not in s[i] or
                'aches' not in s[i] or
                'aching' not in s[i] or
                'acrid' not in s[i] or
                'acridly' not in s[i] or
                'acridness' not in s[i] or
                'acrimonious' not in s[i] or
                'acrimoniously' not in s[i] or
                'acrimony' not in s[i] or
                'adamant' not in s[i] or
                'adamantly' not in s[i] or
                'addict' not in s[i] or
                'addicted' not in s[i] or
                'addicting' not in s[i] or
                'addicts' not in s[i] or
                'admonish' not in s[i] or
                'admonisher' not in s[i] or
                'admonishingly' not in s[i] or
                'admonis…' not in s[i] or
                'babble' not in s[i] or
                'back-logged' not in s[i] or
                'back-wood' not in s[i] or
                'back-woods' not in s[i] or
                'backache' not in s[i] or
                'backaches' not in s[i] or
                'backbite' not in s[i] or
                'backbiting' not in s[i] or
                'backward' not in s[i] or
                'backwardness' not in s[i] or
                'backwoods' not in s[i] or
                'bad' not in s[i] or
                'badly' not in s[i] or
                'baffle' not in s[i] or
                'baffled' not in s[i] or
                'bafflement' not in s[i] or
                'baffling' not in s[i] or
                'bait' not in s[i] or
                'balk' not in s[i] or
                'banal' not in s[i] or
                'bane' not in s[i] or
                'banish' not in s[i] or
                'banishment' not in s[i] or
                'bankrupt' not in s[i] or
                'barbarian' not in s[i] or
                'barbaric' not in s[i] or
                'barbarically' not in s[i] or
                'barbarity' not in s[i] or
                'barbarous' not in s[i] or
                'barbarously' not in s[i] or
                'barren' not in s[i] or
                'baseless' not in s[i] or
                'bash' not in s[i] or
                'bashed' not in s[i] or
                'bashful' not in s[i] or
                'bashing' not in s[i] or
                'battered' not in s[i] or
                'battering' not in s[i] or
                'batty' not in s[i] or
                'bearish' not in s[i] or
                'beastly' not in s[i] or
                'bedlam' not in s[i] or
                'bedlamite' not in s[i] or
                'befoul' not in s[i] or
                'beg' not in s[i] or
                'beggar' not in s[i] or
                'beggarly' not in s[i] or
                'begging' not in s[i] or
                'beguile' not in s[i] or
                'belabor' not in s[i] or
                'belated' not in s[i] or
                'beleaguer' not in s[i] or
                'belie' not in s[i] or
                'belittle' not in s[i] or
                'belittled' not in s[i] or
                'belittling' not in s[i] or
                'bellicose' not in s[i] or
                'belligerence' not in s[i] or
                'belligerent' not in s[i] or
                'belligerently' not in s[i] or
                '…' not in s[i] or
                'cackle' not in s[i] or
                'calamities' not in s[i] or
                'calamitous' not in s[i] or
                'calamitously' not in s[i] or
                'calamity' not in s[i] or
                'callous' not in s[i] or
                'calumniate' not in s[i] or
                'calumniation' not in s[i] or
                'calumnies' not in s[i] or
                'calumnious' not in s[i] or
                'calumniously' not in s[i] or
                'calumny' not in s[i] or
                'cancer' not in s[i] or
                'cancerous' not in s[i] or
                'cannibal' not in s[i] or
                'cannibalize' not in s[i] or
                'capitulate' not in s[i] or
                'capricious' not in s[i] or
                'capriciously' not in s[i] or
                'capriciousness' not in s[i] or
                'capsize' not in s[i] or
                'careless' not in s[i] or
                'carelessness' not in s[i] or
                'caricature' not in s[i] or
                'carnage' not in s[i] or
                'carp' not in s[i] or
                'cartoonish' not in s[i] or
                'cash-strapped' not in s[i] or
                'castigate' not in s[i] or
                'castrated' not in s[i] or
                'casualty' not in s[i] or
                'cataclysm' not in s[i] or
                'cataclysmal' not in s[i] or
                'cataclysmic' not in s[i] or
                'cataclysmically' not in s[i] or
                'catastrophe' not in s[i] or
                'catastrophes' not in s[i] or
                'catastrophic' not in s[i] or
                'catastrophically' not in s[i] or
                'caustic' not in s[i] or
                'caustically' not in s[i] or
                'cautionary' not in s[i] or
                'cave' not in s[i] or
                'censure' not in s[i] or
                'chafe' not in s[i] or
                'chaff' not in s[i] or
                'chagrin' not in s[i] or
                'challenging' not in s[i] or
                'chaos' not in s[i] or
                'chaotic' not in s[i] or
                'chasten' not in s[i] or
                'chastise' not in s[i] or
                'chastisement' not in s[i] or
                'chatte…' not in s[i] or
                'damage' not in s[i] or
                'damaged' not in s[i] or
                'damages' not in s[i] or
                'damaging' not in s[i] or
                'damn' not in s[i] or
                'damnable' not in s[i] or
                'damnably' not in s[i] or
                'damnation' not in s[i] or
                'damned' not in s[i] or
                'damning' not in s[i] or
                'damper' not in s[i] or
                'danger' not in s[i] or
                'dangerous' not in s[i] or
                'dangerousness' not in s[i] or
                'dark' not in s[i] or
                'darken' not in s[i] or
                'darkened' not in s[i] or
                'darker' not in s[i] or
                'darkness' not in s[i] or
                'dastard' not in s[i] or
                'dastardly' not in s[i] or
                'daunt' not in s[i] or
                'daunting' not in s[i] or
                'dauntingly' not in s[i] or
                'dawdle' not in s[i] or
                'daze' not in s[i] or
                'dazed' not in s[i] or
                'dead' not in s[i] or
                'deadbeat' not in s[i] or
                'deadlock' not in s[i] or
                'deadly' not in s[i] or
                'deadweight' not in s[i] or
                'deaf' not in s[i] or
                'dearth' not in s[i] or
                'death' not in s[i] or
                'debacle' not in s[i] or
                'debase' not in s[i] or
                'debasement' not in s[i] or
                'debaser' not in s[i] or
                'debatable' not in s[i] or
                'debauch' not in s[i] or
                'debaucher' not in s[i] or
                'debauchery' not in s[i] or
                'debilitate' not in s[i] or
                'debilitating' not in s[i] or
                'debility' not in s[i] or
                'debt' not in s[i] or
                'debts' not in s[i] or
                'decadence' not in s[i] or
                'decadent' not in s[i] or
                'decay' not in s[i] or
                'decayed' not in s[i] or
                'deceit' not in s[i] or
                'deceitful' not in s[i] or
                'deceitfully' not in s[i] or
                'deceitfulness' not in s[i] or
                'deceive' not in s[i] or
                'deceiver' not in s[i] or
                'deceivers' not in s[i] or
                'deceiving' not in s[i] or
                'deception' not in s[i] or
                'deceptiv…' not in s[i] or
                'earsplitting' not in s[i] or
                'eccentric' not in s[i] or
                'eccentricity' not in s[i] or
                'effigy' not in s[i] or
                'effrontery' not in s[i] or
                'egocentric' not in s[i] or
                'egomania' not in s[i] or
                'egotism' not in s[i] or
                'egotistical' not in s[i] or
                'egotistically' not in s[i] or
                'egregious' not in s[i] or
                'egregiously' not in s[i] or
                'election-rigger' not in s[i] or
                'elimination' not in s[i] or
                'emaciated' not in s[i] or
                'emasculate' not in s[i] or
                'embarrass' not in s[i] or
                'embarrassing' not in s[i] or
                'embarrassingly' not in s[i] or
                'embarrassment' not in s[i] or
                'embattled' not in s[i] or
                'embroil' not in s[i] or
                'embroiled' not in s[i] or
                'embroilment' not in s[i] or
                'emergency' not in s[i] or
                'emphatic' not in s[i] or
                'emphatically' not in s[i] or
                'emptiness' not in s[i] or
                'encroach' not in s[i] or
                'encroachment' not in s[i] or
                'endanger' not in s[i] or
                'enemies' not in s[i] or
                'enemy' not in s[i] or
                'enervate' not in s[i] or
                'enfeeble' not in s[i] or
                'enflame' not in s[i] or
                'engulf' not in s[i] or
                'enjoin' not in s[i] or
                'enmity' not in s[i] or
                'enrage' not in s[i] or
                'enraged' not in s[i] or
                'enraging' not in s[i] or
                'enslave' not in s[i] or
                'entangle' not in s[i] or
                'entanglement' not in s[i] or
                'entrap' not in s[i] or
                'entrapment' not in s[i] or
                'envious' not in s[i] or
                'enviously' not in s[i] or
                'enviousness' not in s[i] or
                'epidemic' not in s[i] or
                'equivocal' not in s[i] or
                'erase' not in s[i] or
                'erode' not in s[i] or
                'erodes' not in s[i] or
                'ero…' not in s[i] or
                'f ** k' not in s[i] or
                'fabricate' not in s[i] or
                'fabrication' not in s[i] or
                'facetious' not in s[i] or
                'facetiously' not in s[i] or
                'fail' not in s[i] or
                'failed' not in s[i] or
                'failing' not in s[i] or
                'fails' not in s[i] or
                'failure' not in s[i] or
                'failures' not in s[i] or
                'faint' not in s[i] or
                'fainthearted' not in s[i] or
                'faithless' not in s[i] or
                'fake' not in s[i] or
                'fall' not in s[i] or
                'fallacies' not in s[i] or
                'fallacious' not in s[i] or
                'fallaciously' not in s[i] or
                'fallaciousness' not in s[i] or
                'fallacy' not in s[i] or
                'fallen' not in s[i] or
                'falling' not in s[i] or
                'fallout' not in s[i] or
                'falls' not in s[i] or
                'FALSE' not in s[i] or
                'falsehood' not in s[i] or
                'falsely' not in s[i] or
                'falsify' not in s[i] or
                'falter' not in s[i] or
                'faltered' not in s[i] or
                'famine' not in s[i] or
                'famished' not in s[i] or
                'fanatic' not in s[i] or
                'fanatical' not in s[i] or
                'fanatically' not in s[i] or
                'fanaticism' not in s[i] or
                'fanatics' not in s[i] or
                'fanciful' not in s[i] or
                'far-fetched' not in s[i] or
                'farce' not in s[i] or
                'farcical' not in s[i] or
                'farcical-yet-provocative' not in s[i] or
                'farcically' not in s[i] or
                'farfetched' not in s[i] or
                'fascism' not in s[i] or
                'fascist' not in s[i] or
                'fastidious' not in s[i] or
                'fastidiously' not in s[i] or
                'fat' not in s[i] or
                'fat-cat' not in s[i] or
                'fat-cats' not in s[i] or
                'fatal' not in s[i] or
                'fatalistic' not in s[i] or
                'fatalistically' not in s[i] or
                'fatally' not in s[i] or
                'fateful' not in s[i] or
                'fatefully' not in s[i] or
                'fat…' not in s[i] or
                'gabble' not in s[i] or
                'gaff' not in s[i] or
                'gaffe' not in s[i] or
                'gainsay' not in s[i] or
                'gainsayer' not in s[i] or
                'gall' not in s[i] or
                'galling' not in s[i] or
                'gallingly' not in s[i] or
                'galls' not in s[i] or
                'gangster' not in s[i] or
                'gape' not in s[i] or
                'garbage' not in s[i] or
                'garish' not in s[i] or
                'gasp' not in s[i] or
                'gauche' not in s[i] or
                'gaudy' not in s[i] or
                'gawk' not in s[i] or
                'gawky' not in s[i] or
                'geezer' not in s[i] or
                'genocide' not in s[i] or
                'get-rich' not in s[i] or
                'ghastly' not in s[i] or
                'ghetto' not in s[i] or
                'ghosting' not in s[i] or
                'gibber' not in s[i] or
                'gibberish' not in s[i] or
                'gibe' not in s[i] or
                'giddy' not in s[i] or
                'gimmick' not in s[i] or
                'gimmicked' not in s[i] or
                'gimmicking' not in s[i] or
                'gimmicks' not in s[i] or
                'gimmicky' not in s[i] or
                'glare' not in s[i] or
                'glaringly' not in s[i] or
                'glib' not in s[i] or
                'glibly' not in s[i] or
                'glitch' not in s[i] or
                'glitches' not in s[i] or
                'gloatingly' not in s[i] or
                'gloom' not in s[i] or
                'gloomy' not in s[i] or
                'glower' not in s[i] or
                'glum' not in s[i] or
                'glut' not in s[i] or
                'gnawing' not in s[i] or
                'goad' not in s[i] or
                'goading' not in s[i] or
                'god-awful' not in s[i] or
                'goof' not in s[i] or
                'goofy' not in s[i] or
                'goon' not in s[i] or
                'gossip' not in s[i] or
                'graceless' not in s[i] or
                'gracelessly' not in s[i] or
                'graft' not in s[i] or
                'grainy' not in s[i] or
                'grapple' not in s[i] or
                'grate' not in s[i] or
                'grating' not in s[i] or
                'gravely' not in s[i] or
                'greasy' not in s[i] or
                'greed' not in s[i] or
                'greedy' not in s[i] or
                'grief' not in s[i] or
                'grievance' not in s[i] or
                'grievances' not in s[i] or
                'gr…' not in s[i] or
                'hack' not in s[i] or
                'hacks' not in s[i] or
                'haggard' not in s[i] or
                'haggle' not in s[i] or
                'halfhearted' not in s[i] or
                'halfheartedly' not in s[i] or
                'hallucinate' not in s[i] or
                'hallucination' not in s[i] or
                'hamper' not in s[i] or
                'hampered' not in s[i] or
                'handicapped' not in s[i] or
                'hang' not in s[i] or
                'hangs' not in s[i] or
                'haphazard' not in s[i] or
                'hapless' not in s[i] or
                'harangue' not in s[i] or
                'harass' not in s[i] or
                'harassed' not in s[i] or
                'harasses' not in s[i] or
                'harassment' not in s[i] or
                'harboring' not in s[i] or
                'harbors' not in s[i] or
                'hard' not in s[i] or
                'hard-hit' not in s[i] or
                'hard-liner' not in s[i] or
                'hardball' not in s[i] or
                'harden' not in s[i] or
                'hardened' not in s[i] or
                'hardheaded' not in s[i] or
                'hardhearted' not in s[i] or
                'hardliner' not in s[i] or
                'hardliners' not in s[i] or
                'hardship' not in s[i] or
                'hardships' not in s[i] or
                'harm' not in s[i] or
                'harmed' not in s[i] or
                'harmful' not in s[i] or
                'harms' not in s[i] or
                'harpy' not in s[i] or
                'harridan' not in s[i] or
                'harried' not in s[i] or
                'harrow' not in s[i] or
                'harsh' not in s[i] or
                'harshly' not in s[i] or
                'hassle' not in s[i] or
                'hassled' not in s[i] or
                'hassles' not in s[i] or
                'haste' not in s[i] or
                'hastily' not in s[i] or
                'hasty' not in s[i] or
                'hate' not in s[i] or
                'hated' not in s[i] or
                'hateful' not in s[i] or
                'hatefully' not in s[i] or
                'hatefulness' not in s[i] or
                'hater' not in s[i] or
                'haters' not in s[i] or
                'hates' not in s[i] or
                'hating' not in s[i] or
                'hatred' not in s[i] or
                'haughtily' not in s[i] or
                'haughty' not in s[i] or
                'haun…' not in s[i] or
                'idiocies' not in s[i] or
                'idiocy' not in s[i] or
                'idiot' not in s[i] or
                'idiotic' not in s[i] or
                'idiotically' not in s[i] or
                'idiots' not in s[i] or
                'idle' not in s[i] or
                'ignoble' not in s[i] or
                'ignominious' not in s[i] or
                'ignominiously' not in s[i] or
                'ignominy' not in s[i] or
                'ignorance' not in s[i] or
                'ignorant' not in s[i] or
                'ignore' not in s[i] or
                'ill-advised' not in s[i] or
                'ill-conceived' not in s[i] or
                'ill-defined' not in s[i] or
                'ill-designed' not in s[i] or
                'ill-fated' not in s[i] or
                'ill-favored' not in s[i] or
                'ill-formed' not in s[i] or
                'ill-mannered' not in s[i] or
                'ill-natured' not in s[i] or
                'ill-sorted' not in s[i] or
                'ill-tempered' not in s[i] or
                'ill-treated' not in s[i] or
                'ill-treatment' not in s[i] or
                'ill-usage' not in s[i] or
                'ill-used' not in s[i] or
                'illegal' not in s[i] or
                'illegally' not in s[i] or
                'illegitimate' not in s[i] or
                'illicit' not in s[i] or
                'illiterate' not in s[i] or
                'illness' not in s[i] or
                'illogical' not in s[i] or
                'illogically' not in s[i] or
                'illusion' not in s[i] or
                'illusions' not in s[i] or
                'illusory' not in s[i] or
                'imaginary' not in s[i] or
                'imbalance' not in s[i] or
                'imbecile' not in s[i] or
                'imbroglio' not in s[i] or
                'immaterial' not in s[i] or
                'immature' not in s[i] or
                'imminence' not in s[i] or
                'imminently' not in s[i] or
                'immobilized' not in s[i] or
                'immoderate' not in s[i] or
                'immoderately' not in s[i] or
                'immodest' not in s[i] or
                'immoral' not in s[i] or
                'immorality' not in s[i] or
                'jabber' not in s[i] or
                'jaded' not in s[i] or
                'jagged' not in s[i] or
                'jam' not in s[i] or
                'jarring' not in s[i] or
                'jaundiced' not in s[i] or
                'jealous' not in s[i] or
                'jealously' not in s[i] or
                'jealousness' not in s[i] or
                'jealousy' not in s[i] or
                'jeer' not in s[i] or
                'jeering' not in s[i] or
                'jeeringly' not in s[i] or
                'jeers' not in s[i] or
                'jeopardize' not in s[i] or
                'jeopardy' not in s[i] or
                'jerk' not in s[i] or
                'jerky' not in s[i] or
                'jitter' not in s[i] or
                'jitters' not in s[i] or
                'jittery' not in s[i] or
                'job-killing' not in s[i] or
                'jobless' not in s[i] or
                'joke' not in s[i] or
                'joker' not in s[i] or
                'jolt' not in s[i] or
                'judder' not in s[i] or
                'juddering' not in s[i] or
                'judders' not in s[i] or
                'jumpy' not in s[i] or
                'junk' not in s[i] or
                'junky' not in s[i] or
                'junkyard' not in s[i] or
                'kill' not in s[i] or
                'killed' not in s[i] or
                'killer' not in s[i] or
                'killing' not in s[i] or
                'killjoy' not in s[i] or
                'kills' not in s[i] or
                'knave' not in s[i] or
                'knife' not in s[i] or
                'knock' not in s[i] or
                'knotted' not in s[i] or
                'kook' not in s[i] or
                'kooky' not in s[i] or
                'lack' not in s[i] or
                'lackadaisical' not in s[i] or
                'lacked' not in s[i] or
                'lackey' not in s[i] or
                'lackeys' not in s[i] or
                'lacking' not in s[i] or
                'lackluster' not in s[i] or
                'lacks' not in s[i] or
                'laconic' not in s[i] or
                'lag' not in s[i] or
                'lagged' not in s[i] or
                'lagging' not in s[i] or
                'lags' not in s[i] or
                'laid-off' not in s[i] or
                'lambast' not in s[i] or
                'lambaste' not in s[i] or
                'lame' not in s[i] or
                'lame-duck' not in s[i] or
                'lament' not in s[i] or
                'lamentable' not in s[i] or
                'lamentably' not in s[i] or
                'languid' not in s[i] or
                'languish' not in s[i] or
                'languor' not in s[i] or
                'languorous' not in s[i] or
                'languorously' not in s[i] or
                'lanky' not in s[i] or
                'lapse' not in s[i] or
                'lapsed' not in s[i] or
                'lapses' not in s[i] or
                'lascivious' not in s[i] or
                'last-ditch' not in s[i] or
                'latency' not in s[i] or
                'laughable' not in s[i] or
                'laughably' not in s[i] or
                'laughingstock' not in s[i] or
                'lawbreaker' not in s[i] or
                'lawbreaking' not in s[i] or
                'lawless' not in s[i] or
                'lawlessness' not in s[i] or
                'layoff' not in s[i] or
                'layoff-happy' not in s[i] or
                'lazy' not in s[i] or
                'leak' not in s[i] or
                'leakage' not in s[i] or
                'leakages' not in s[i] or
                'leaking' not in s[i] or
                'leaks' not in s[i] or
                'leaky' not in s[i] or
                'lecher' not in s[i] or
                'lecherous' not in s[i] or
                'lechery' not in s[i] or
                'leech' not in s[i] or
                'leer' not in s[i] or
                'leery' not in s[i] or
                'left-leaning' not in s[i] or
                'lemon' not in s[i] or
                'lengthy' not in s[i] or
                'less-developed' not in s[i] or
                'lesser-known' not in s[i] or
                'letch' not in s[i] or
                'leth…' not in s[i] or
                'macabre' not in s[i] or
                'mad' not in s[i] or
                'madden' not in s[i] or
                'maddening' not in s[i] or
                'maddeningly' not in s[i] or
                'madder' not in s[i] or
                'madly' not in s[i] or
                'madman' not in s[i] or
                'madness' not in s[i] or
                'maladjusted' not in s[i] or
                'maladjustment' not in s[i] or
                'malady' not in s[i] or
                'malaise' not in s[i] or
                'malcontent' not in s[i] or
                'malcontented' not in s[i] or
                'maledict' not in s[i] or
                'malevolence' not in s[i] or
                'malevolent' not in s[i] or
                'malevolently' not in s[i] or
                'malice' not in s[i] or
                'malicious' not in s[i] or
                'maliciously' not in s[i] or
                'maliciousness' not in s[i] or
                'malign' not in s[i] or
                'malignant' not in s[i] or
                'malodorous' not in s[i] or
                'maltreatment' not in s[i] or
                'mangle' not in s[i] or
                'mangled' not in s[i] or
                'mangles' not in s[i] or
                'mangling' not in s[i] or
                'mania' not in s[i] or
                'maniac' not in s[i] or
                'maniacal' not in s[i] or
                'manic' not in s[i] or
                'manipulate' not in s[i] or
                'manipulation' not in s[i] or
                'manipulative' not in s[i] or
                'manipulators' not in s[i] or
                'mar' not in s[i] or
                'marginal' not in s[i] or
                'marginally' not in s[i] or
                'martyrdom' not in s[i] or
                'martyrdom-seeking' not in s[i] or
                'mashed' not in s[i] or
                'massacre' not in s[i] or
                'massacres' not in s[i] or
                'matte' not in s[i] or
                'mawkish' not in s[i] or
                'mawkishly' not in s[i] or
                'mawkishness' not in s[i] or
                'meager' not in s[i] or
                'meaningless' not in s[i] or
                'meanness' not in s[i] or
                'measly' not in s[i] or
                'meddle' not in s[i] or
                'meddlesome' not in s[i] or
                'nag' not in s[i] or
                'nagging' not in s[i] or
                'naive' not in s[i] or
                'naively' not in s[i] or
                'narrower' not in s[i] or
                'nastily' not in s[i] or
                'nastiness' not in s[i] or
                'nasty' not in s[i] or
                'naughty' not in s[i] or
                'nauseate' not in s[i] or
                'nauseates' not in s[i] or
                'nauseating' not in s[i] or
                'nauseatingly' not in s[i] or
                'naïve' not in s[i] or
                'nebulous' not in s[i] or
                'nebulously' not in s[i] or
                'needless' not in s[i] or
                'needlessly' not in s[i] or
                'needy' not in s[i] or
                'nefarious' not in s[i] or
                'nefariously' not in s[i] or
                'negate' not in s[i] or
                'negation' not in s[i] or
                'negative' not in s[i] or
                'negatives' not in s[i] or
                'negativity' not in s[i] or
                'neglect' not in s[i] or
                'neglected' not in s[i] or
                'negligence' not in s[i] or
                'negligent' not in s[i] or
                'nemesis' not in s[i] or
                'nepotism' not in s[i] or
                'nervous' not in s[i] or
                'nervously' not in s[i] or
                'nervousness' not in s[i] or
                'nettle' not in s[i] or
                'nettlesome' not in s[i] or
                'neurotic' not in s[i] or
                'neurotically' not in s[i] or
                'niggle' not in s[i] or
                'niggles' not in s[i] or
                'nightmare' not in s[i] or
                'nightmarish' not in s[i] or
                'nightmarishly' not in s[i] or
                'nitpick' not in s[i] or
                'nitpicking' not in s[i] or
                'noise' not in s[i] or
                'noises' not in s[i] or
                'noisier' not in s[i] or
                'noisy' not in s[i] or
                'non-confidence' not in s[i] or
                'nonexistent' not in s[i] or
                'nonresponsive' not in s[i] or
                'nonsense' not in s[i] or
                'nosey' not in s[i] or
                'notoriety' not in s[i] or
                'notorious' not in s[i] or
                'notoriously' not in s[i] or
                'noxious' not in s[i] or
                'nuisance' not in s[i] or
                'numb' not in s[i] or
                'obese' not in s[i] or
                'object' not in s[i] or
                'objection' not in s[i] or
                'objectionable' not in s[i] or
                'objections' not in s[i] or
                'oblique' not in s[i] or
                'obliterate' not in s[i] or
                'obliterated' not in s[i] or
                'oblivious' not in s[i] or
                'obnoxious' not in s[i] or
                'obnoxiously' not in s[i] or
                'obscene' not in s[i] or
                'obscenely' not in s[i] or
                'obscenity' not in s[i] or
                'obscure' not in s[i] or
                'obscured' not in s[i] or
                'obscures' not in s[i] or
                'obscurity' not in s[i] or
                'obsess' not in s[i] or
                'obsessive' not in s[i] or
                'obsessively' not in s[i] or
                'obsessiveness' not in s[i] or
                'obsolete' not in s[i] or
                'obstacle' not in s[i] or
                'obstinate' not in s[i] or
                'obstinately' not in s[i] or
                'obstruct' not in s[i] or
                'obstructed' not in s[i] or
                'obstructing' not in s[i] or
                'obstruction' not in s[i] or
                'obstructs' not in s[i] or
                'obtrusive' not in s[i] or
                'obtuse' not in s[i] or
                'occlude' not in s[i] or
                'occluded' not in s[i] or
                'occludes' not in s[i] or
                'occluding' not in s[i] or
                'odd' not in s[i] or
                'odder' not in s[i] or
                'oddest' not in s[i] or
                'oddities' not in s[i] or
                'oddity' not in s[i] or
                'oddly' not in s[i] or
                'odor' not in s[i] or
                'offence' not in s[i] or
                'offend' not in s[i] or
                'offender' not in s[i] or
                'offending' not in s[i] or
                'offenses' not in s[i] or
                'offensive' not in s[i] or
                'offensively' not in s[i] or
                'offensiveness' not in s[i] or
                'officious' not in s[i] or
                'ominous' not in s[i] or
                'ominously' not in s[i] or
                'omission' not in s[i] or
                'omit' not in s[i] or
                'one-sided' not in s[i] or
                'pain' not in s[i] or
                'painful' not in s[i] or
                'painfully' not in s[i] or
                'pains' not in s[i] or
                'pale' not in s[i] or
                'pales' not in s[i] or
                'paltry' not in s[i] or
                'pan' not in s[i] or
                'pandemonium' not in s[i] or
                'pander' not in s[i] or
                'pandering' not in s[i] or
                'panders' not in s[i] or
                'panic' not in s[i] or
                'panicked' not in s[i] or
                'panicking' not in s[i] or
                'panicky' not in s[i] or
                'paradoxical' not in s[i] or
                'paradoxically' not in s[i] or
                'paralyzed' not in s[i] or
                'paranoia' not in s[i] or
                'paranoid' not in s[i] or
                'parasite' not in s[i] or
                'pariah' not in s[i] or
                'parody' not in s[i] or
                'partiality' not in s[i] or
                'partisan' not in s[i] or
                'partisans' not in s[i] or
                'passive' not in s[i] or
                'passiveness' not in s[i] or
                'pathetic' not in s[i] or
                'pathetically' not in s[i] or
                'patronize' not in s[i] or
                'paucity' not in s[i] or
                'pauper' not in s[i] or
                'paupers' not in s[i] or
                'payback' not in s[i] or
                'peculiar' not in s[i] or
                'peculiarly' not in s[i] or
                'pedantic' not in s[i] or
                'peeled' not in s[i] or
                'peeve' not in s[i] or
                'peeved' not in s[i] or
                'peevish' not in s[i] or
                'peevishly' not in s[i] or
                'penalize' not in s[i] or
                'penalty' not in s[i] or
                'perfidious' not in s[i] or
                'perfunctory' not in s[i] or
                'peril' not in s[i] or
                'perilous' not in s[i] or
                'perilously' not in s[i] or
                'perish' not in s[i] or
                'pernicious' not in s[i] or
                'perplex' not in s[i] or
                'perplexed' not in s[i] or
                'perplexing' not in s[i] or
                'perplexity' not in s[i] or
                'persecute' not in s[i] or
                'persecution' not in s[i] or
                'quack' not in s[i] or
                'qualm' not in s[i] or
                'qualms' not in s[i] or
                'quandary' not in s[i] or
                'quarrel' not in s[i] or
                'quarrels' not in s[i] or
                'quarrelsome' not in s[i] or
                'quash' not in s[i] or
                'queer' not in s[i] or
                'questionable' not in s[i] or
                'quibble' not in s[i] or
                'quibbles' not in s[i] or
                'quitter' not in s[i] or
                'rabid' not in s[i] or
                'racism' not in s[i] or
                'racist' not in s[i] or
                'racists' not in s[i] or
                'racy' not in s[i] or
                'radical' not in s[i] or
                'radicalization' not in s[i] or
                'radically' not in s[i] or
                'radicals' not in s[i] or
                'rage' not in s[i] or
                'ragged' not in s[i] or
                'raging' not in s[i] or
                'rail' not in s[i] or
                'raked' not in s[i] or
                'rampage' not in s[i] or
                'rampant' not in s[i] or
                'ramshackle' not in s[i] or
                'rancor' not in s[i] or
                'randomly' not in s[i] or
                'rankle' not in s[i] or
                'rant' not in s[i] or
                'ranted' not in s[i] or
                'ranting' not in s[i] or
                'rants' not in s[i] or
                'rape' not in s[i] or
                'raped' not in s[i] or
                'raping' not in s[i] or
                'rascal' not in s[i] or
                'rascals' not in s[i] or
                'rash' not in s[i] or
                'rattle' not in s[i] or
                'rattled' not in s[i] or
                'rattles' not in s[i] or
                'ravage' not in s[i] or
                'raving' not in s[i] or
                'reactionary' not in s[i] or
                'rebellious' not in s[i] or
                'rebuff' not in s[i] or
                'rebuke' not in s[i] or
                'recalcitrant' not in s[i] or
                'recant' not in s[i] or
                'recession' not in s[i] or
                'recessionary' not in s[i] or
                'reckless' not in s[i] or
                'recklessly' not in s[i] or
                'recklessness' not in s[i] or
                'recoil' not in s[i] or
                'recourses' not in s[i] or
                'redundancy' not in s[i] or
                'redundant' not in s[i] or
                'refusal' not in s[i] or
                'refuse' not in s[i] or
                'refused' not in s[i] or
                'refuses' not in s[i] or
                'refusing' not in s[i] or
                'refutation' not in s[i] or
                'refute' not in s[i] or
                'refuted' not in s[i] or
                'refutes' not in s[i] or
                'refuting' not in s[i] or
                'regress' not in s[i] or
                'regression' not in s[i] or
                'regressive' not in s[i] or
                'sabotage' not in s[i] or
                'sack' not in s[i] or
                'sacrificed' not in s[i] or
                'sad' not in s[i] or
                'sadden' not in s[i] or
                'sadly' not in s[i] or
                'sadness' not in s[i] or
                'sag' not in s[i] or
                'sagged' not in s[i] or
                'sagging' not in s[i] or
                'saggy' not in s[i] or
                'sags' not in s[i] or
                'salacious' not in s[i] or
                'sanctimonious' not in s[i] or
                'sap' not in s[i] or
                'sarcasm' not in s[i] or
                'sarcastic' not in s[i] or
                'sarcastically' not in s[i] or
                'sardonic' not in s[i] or
                'sardonically' not in s[i] or
                'sass' not in s[i] or
                'satirical' not in s[i] or
                'satirize' not in s[i] or
                'savage' not in s[i] or
                'savaged' not in s[i] or
                'savagery' not in s[i] or
                'savages' not in s[i] or
                'scaly' not in s[i] or
                'scam' not in s[i] or
                'scams' not in s[i] or
                'scandal' not in s[i] or
                'scandalize' not in s[i] or
                'scandalized' not in s[i] or
                'scandalous' not in s[i] or
                'scandalously' not in s[i] or
                'scandals' not in s[i] or
                'scant' not in s[i] or
                'scapegoat' not in s[i] or
                'scar' not in s[i] or
                'scarce' not in s[i] or
                'scarcely' not in s[i] or
                'scarcity' not in s[i] or
                'scare' not in s[i] or
                'scared' not in s[i] or
                'scarier' not in s[i] or
                'scariest' not in s[i] or
                'scarily' not in s[i] or
                'scarred' not in s[i] or
                'scars' not in s[i] or
                'scary' not in s[i] or
                'scathing' not in s[i] or
                'scathingly' not in s[i] or
                'scoff' not in s[i] or
                'scold' not in s[i] or
                'scolded' not in s[i] or
                'scolding' not in s[i] or
                'scorching' not in s[i] or
                'scorn' not in s[i] or
                'scornful' not in s[i] or
                'scornfully' not in s[i] or
                'scoundrel' not in s[i] or
                'scourge' not in s[i] or
                'scowl' not in s[i] or
                'taboo' not in s[i] or
                'tacky' not in s[i] or
                'taint' not in s[i] or
                'tainted' not in s[i] or
                'tamper' not in s[i] or
                'tangle' not in s[i] or
                'tangled' not in s[i] or
                'tangles' not in s[i] or
                'tank' not in s[i] or
                'tanked' not in s[i] or
                'tanks' not in s[i] or
                'tantrum' not in s[i] or
                'tardy' not in s[i] or
                'tarnish' not in s[i] or
                'tarnished' not in s[i] or
                'tarnishes' not in s[i] or
                'tarnishing' not in s[i] or
                'tattered' not in s[i] or
                'taunt' not in s[i] or
                'taunting' not in s[i] or
                'tauntingly' not in s[i] or
                'taunts' not in s[i] or
                'taut' not in s[i] or
                'tawdry' not in s[i] or
                'taxing' not in s[i] or
                'tease' not in s[i] or
                'teasingly' not in s[i] or
                'tedious' not in s[i] or
                'tediously' not in s[i] or
                'temerity' not in s[i] or
                'temper' not in s[i] or
                'tempest' not in s[i] or
                'temptation' not in s[i] or
                'tenderness' not in s[i] or
                'tense' not in s[i] or
                'tension' not in s[i] or
                'tentative' not in s[i] or
                'tentatively' not in s[i] or
                'tenuous' not in s[i] or
                'tenuously' not in s[i] or
                'tepid' not in s[i] or
                'terrible' not in s[i] or
                'terribleness' not in s[i] or
                'terribly' not in s[i] or
                'terror' not in s[i] or
                'terror-genic' not in s[i] or
                'terrorism' not in s[i] or
                'terrorize' not in s[i] or
                'testily' not in s[i] or
                'testy' not in s[i] or
                'tetchily' not in s[i] or
                'tetchy' not in s[i] or
                'thankless' not in s[i] or
                'thicker' not in s[i] or
                'thirst' not in s[i] or
                'thorny' not in s[i] or
                'thoughtless' not in s[i] or
                'thoughtlessly' not in s[i] or
                'thoughtlessness' not in s[i] or
                'thrash' not in s[i] or
                'threat' not in s[i] or
                'threate…' not in s[i] or
                'ugh' not in s[i] or
                'uglier' not in s[i] or
                'ugliest' not in s[i] or
                'ugliness' not in s[i] or
                'ugly' not in s[i] or
                'ulterior' not in s[i] or
                'ultimatum' not in s[i] or
                'ultimatums' not in s[i] or
                'ultra-hardline' not in s[i] or
                'un-viewable' not in s[i] or
                'unable' not in s[i] or
                'unacceptable' not in s[i] or
                'unacceptably' not in s[i] or
                'unaccustomed' not in s[i] or
                'unachievable' not in s[i] or
                'unaffordable' not in s[i] or
                'unappealing' not in s[i] or
                'unattractive' not in s[i] or
                'unauthentic' not in s[i] or
                'unavailable' not in s[i] or
                'unavoidably' not in s[i] or
                'unbearable' not in s[i] or
                'unbelievable' not in s[i] or
                'unbelievably' not in s[i] or
                'uncaring' not in s[i] or
                'uncertain' not in s[i] or
                'uncivil' not in s[i] or
                'uncivilized' not in s[i] or
                'unclean' not in s[i] or
                'unclear' not in s[i] or
                'uncollectible' not in s[i] or
                'uncomfortable' not in s[i] or
                'uncomfortably' not in s[i] or
                'uncompetitive' not in s[i] or
                'uncompromising' not in s[i] or
                'uncompromisingly' not in s[i] or
                'unconfirmed' not in s[i] or
                'unconstitutional' not in s[i] or
                'uncontrolled' not in s[i] or
                'unconvincing' not in s[i] or
                'unconvincingly' not in s[i] or
                'uncooperative' not in s[i] or
                'uncouth' not in s[i] or
                'uncreative' not in s[i] or
                'undecided' not in s[i] or
                'undefined' not in s[i] or
                'undependability' not in s[i] or
                'undependable' not in s[i] or
                'undercut' not in s[i] or
                'u…' not in s[i] or
                'vagrant' not in s[i] or
                'vague' not in s[i] or
                'vagueness' not in s[i] or
                'vain' not in s[i] or
                'vainly' not in s[i] or
                'vanity' not in s[i] or
                'vehement' not in s[i] or
                'vehemently' not in s[i] or
                'vengeance' not in s[i] or
                'vengeful' not in s[i] or
                'vengefully' not in s[i] or
                'vengefulness' not in s[i] or
                'venom' not in s[i] or
                'venomous' not in s[i] or
                'venomously' not in s[i] or
                'vent' not in s[i] or
                'vestiges' not in s[i] or
                'vex' not in s[i] or
                'vexation' not in s[i] or
                'vexing' not in s[i] or
                'vexingly' not in s[i] or
                'vibrate' not in s[i] or
                'vibrated' not in s[i] or
                'vibrates' not in s[i] or
                'vibrating' not in s[i] or
                'vibration' not in s[i] or
                'vice' not in s[i] or
                'vicious' not in s[i] or
                'viciously' not in s[i] or
                'viciousness' not in s[i] or
                'victimize' not in s[i] or
                'vile' not in s[i] or
                'vileness' not in s[i] or
                'vilify' not in s[i] or
                'villainous' not in s[i] or
                'villainously' not in s[i] or
                'villains' not in s[i] or
                'vindictive' not in s[i] or
                'vindictively' not in s[i] or
                'vindictiveness' not in s[i] or
                'violate' not in s[i] or
                'violation' not in s[i] or
                'violator' not in s[i] or
                'violators' not in s[i] or
                'violent' not in s[i] or
                'violently' not in s[i] or
                'viper' not in s[i] or
                'virulence' not in s[i] or
                'virulent' not in s[i] or
                'virulently' not in s[i] or
                'virus' not in s[i] or
                'vociferous' not in s[i] or
                'vociferously' not in s[i] or
                'volatile' not in s[i] or
                'volatility' not in s[i] or
                'vomit' not in s[i] or
                'vomited' not in s[i] or
                'vomiting' not in s[i] or
                'vomits' not in s[i] or
                'vulgar' not in s[i] or
                'vulnerable' not in s[i] or
                'wail' not in s[i] or
                'wallow' not in s[i] or
                'wane' not in s[i] or
                'waning' not in s[i] or
                'wanton' not in s[i] or
                'war-like' not in s[i] or
                'warily' not in s[i] or
                'wariness' not in s[i] or
                'warlike' not in s[i] or
                'warned' not in s[i] or
                'warning' not in s[i] or
                'warp' not in s[i] or
                'warped' not in s[i] or
                'wary' not in s[i] or
                'washed-out' not in s[i] or
                'waste' not in s[i] or
                'wasted' not in s[i] or
                'wasteful' not in s[i] or
                'wastefulness' not in s[i] or
                'wasting' not in s[i] or
                'water-down' not in s[i] or
                'watered-down' not in s[i] or
                'wayward' not in s[i] or
                'weak' not in s[i] or
                'weaken' not in s[i] or
                'weakening' not in s[i] or
                'weaker' not in s[i] or
                'weakness' not in s[i] or
                'weaknesses' not in s[i] or
                'weariness' not in s[i] or
                'wearisome' not in s[i] or
                'weary' not in s[i] or
                'wedge' not in s[i] or
                'weed' not in s[i] or
                'weep' not in s[i] or
                'weird' not in s[i] or
                'weirdly' not in s[i] or
                'wheedle' not in s[i] or
                'whimper' not in s[i] or
                'whine' not in s[i] or
                'whining' not in s[i] or
                'whiny' not in s[i] or
                'whips' not in s[i] or
                'wicked' not in s[i] or
                'wickedly' not in s[i] or
                'wickedness' not in s[i] or
                'wild' not in s[i] or
                'wildly' not in s[i] or
                'wiles' not in s[i] or
                'wilt' not in s[i] or
                'wily' not in s[i] or
                'wimpy' not in s[i] or
                'wince' not in s[i] or
                'wobble' not in s[i] or
                'wobbled' not in s[i] or
                'wobbles' not in s[i] or
                'woe' not in s[i] or
                'woebegone' not in s[i] or
                'woeful' not in s[i] or
                'woefully' not in s[i] or
                'womanizer' not in s[i] or
                'womanizing' not in s[i] or
                'worn' not in s[i] or
                'worried' not in s[i] or
                'worriedly' not in s[i] or
                'worrier' not in s[i] or
                'worries' not in s[i] or
                'worrisome' not in s[i] or
                'worry' not in s[i] or
                'worrying' not in s[i] or
                'worryingly' not in s[i] or
                'worse' not in s[i] or
                'worsen' not in s[i] or
                'worsening' not in s[i] or
                'worst' not in s[i] or
                'worthless' not in s[i] or
                'worthlessly' not in s[i] or
                'worthlessness' not in s[i] or
                'wound' not in s[i] or
                'wounds' not in s[i] or
                'wrangle' not in s[i] or
                'wrath' not in s[i] or
                'wreak' not in s[i] or
                'wreaked' not in s[i] or
                'wreaks' not in s[i] or
                'wreck' not in s[i] or
                'wrest' not in s[i] or
                'wrestle' not in s[i] or
                'wretch' not in s[i] or
                'wretched' not in s[i] or
                'wretchedly' not in s[i] or
                'wretchedness' not in s[i] or
                'wrinkle' not in s[i] or
                'wrinkled' not in s[i] or
                'wrinkles' not in s[i] or
                'writhe' not in s[i] or
                'wrong' not in s[i] or
                'wrongful' not in s[i] or
                'wrongly' not in s[i] or
                "good" in s[i] or
                "best" in s[i] or
                "better" in s[i] or
                "nice" in s[i] or
                "perfect" in s[i] or
                "hehe" in s[i] or
                "cheerful" in s[i] or
                'Adaptable' not in s[i] or
                'Adventurous' not in s[i] or
                'Amazing' not in s[i] or
                'Amiable' not in s[i] or
                'Beautiful' not in s[i] or
                'Becoming' not in s[i] or
                'Beloved' not in s[i] or
                'Blessed' not in s[i] or
                'Blissful' not in s[i] or
                'Brotherly' not in s[i] or
                'Calming' not in s[i] or
                'Captivating' not in s[i] or
                'Charming' not in s[i] or
                'Cherished' not in s[i] or
                'Comforting' not in s[i] or
                'Compelling' not in s[i] or
                'Considerable' not in s[i] or
                'Credible' not in s[i] or
                'Dapper' not in s[i] or
                'Darling' not in s[i] or
                'Delicious' not in s[i] or
                'Delightful' not in s[i] or
                'Dependable' not in s[i] or
                'Desirable' not in s[i] or
                'Dreamy' not in s[i] or
                'Durable' not in s[i] or
                'Elegant' not in s[i] or
                'Empowering' not in s[i] or
                'Enchanting' not in s[i] or
                'Endearing' not in s[i] or
                'Energising' not in s[i] or
                'Enjoyable' not in s[i] or
                'Enlightening' not in s[i] or
                'Exceptional' not in s[i] or
                'Fabulous' not in s[i] or
                'Fancy' not in s[i] or
                'Fantastic' not in s[i] or
                'Fashionable' not in s[i] or
                'Faultless' not in s[i] or
                'Fetching' not in s[i] or
                'Flourishing' not in s[i] or
                'Formidable' not in s[i] or
                'Fulfilling' not in s[i] or
                'Funny' not in s[i] or
                'Generous' not in s[i] or
                'Gifted' not in s[i] or
                'Glamorous' not in s[i] or
                'Gleaming' not in s[i] or
                'Glowing' not in s[i] or
                'Godly' not in s[i] or
                'Gracious' not in s[i] or
                'Gratifying' not in s[i] or
                'Happening' not in s[i] or
                'Harmonious' not in s[i] or
                'Heavenly' not in s[i] or
                'Honourable' not in s[i] or
                'Ideal' not in s[i] or
                'Important' not in s[i] or
                'Incredible' not in s[i] or
                'Indispensable' not in s[i] or
                'Indisputable' not in s[i] or
                'Influential' not in s[i] or
                'Inspiring' not in s[i] or
                'Interesting' not in s[i] or
                'Irresistible' not in s[i] or
                'Joyful' not in s[i] or
                'Jolly' not in s[i] or
                'Jovial' not in s[i] or
                'Kindly' not in s[i] or
                'Kingly' not in s[i] or
                'Leading' not in s[i] or
                'Legendary' not in s[i] or
                'Liberating' not in s[i] or
                'Likeable' not in s[i] or
                'Lordly' not in s[i] or
                'Lovable' not in s[i] or
                'Luscious' not in s[i] or
                'Magical' not in s[i] or
                'Majestic' not in s[i] or
                'Memorable' not in s[i] or
                'Mesmerizing' not in s[i] or
                'Mighty' not in s[i] or
                'Miraculous' not in s[i] or
                'Motivational' not in s[i] or
                'Nifty' not in s[i] or
                'Obliging' not in s[i] or
                'Optimal' not in s[i] or
                'Original' not in s[i] or
                'Out' not in s[i] or
                'of' not in s[i] or
                'this' not in s[i] or
                'world' not in s[i] or
                'Outgoing' not in s[i] or
                'Palatable' not in s[i] or
                'Paramount' not in s[i] or
                'Peaceful' not in s[i] or
                'Peachy' not in s[i] or
                'Perfect' not in s[i] or
                'Phenomenal' not in s[i] or
                'Picturesque' not in s[i] or
                'Pleasant' not in s[i] or
                'Pleasing' not in s[i] or
                'Pleasurable' not in s[i] or
                'Positive' not in s[i] or
                'Powerful' not in s[i] or
                'Praiseworthy' not in s[i] or
                'Precious' not in s[i] or
                'Prestigious' not in s[i] or
                'Prizewinning' not in s[i] or
                'Promising' not in s[i] or
                'Quality' not in s[i] or
                'Radiant' not in s[i] or
                'Reasonable' not in s[i] or
                'Refreshing' not in s[i] or
                'Reliable' not in s[i] or
                'Respectable' not in s[i] or
                'Revolutionary' not in s[i] or
                'Rewarding' not in s[i] or
                'Rousing' not in s[i] or
                'Saintly' not in s[i] or
                'Salubrious' not in s[i] or
                'Satisfying' not in s[i] or
                'Scrumptious' not in s[i] or
                'Sensational' not in s[i] or
                'Sexy' not in s[i] or
                'Shiny' not in s[i] or
                'Showy' not in s[i] or
                'Smashing' not in s[i] or
                'Soothing' not in s[i] or
                'Sought-after' not in s[i] or
                'Spectacular' not in s[i] or
                'Spiffy' not in s[i] or
                'Stimulating' not in s[i] or
                'Striking' not in s[i] or
                'Stunning' not in s[i] or
                'Stupendous' not in s[i] or
                'Superb' not in s[i] or
                'Supreme' not in s[i] or
                'Swanky' not in s[i] or
                'Tasteful' not in s[i] or
                'Tasty' not in s[i] or
                'Terrific' not in s[i] or
                'Thrilling' not in s[i] or
                'Titillating' not in s[i] or
                'Tremendous' not in s[i] or
                'Trusty' not in s[i] or
                'Ultimate' not in s[i] or
                'Unbelievable' not in s[i] or
                'Uplifting' not in s[i] or
                'Useful' not in s[i] or
                'Valuable' not in s[i] or
                'Vibrant' not in s[i] or
                'wrought'not in s[i]):
                print(s[i],"\nthis comment seems to be neutral")
                g+=1
    print(f"there were total{g}neutral comments")
#====================main code==============================#
try:
    j=0
    while True:
        if(j!=0):
            user=(input("""if you want to continue then 
            Enter your choice from the below options 
            \n1.positive\n2.negative\n3.neutral\n4.br
            (to break the operation)  here->\t"""))
        else:
            user = (input("""Enter your choice from the below options 
                        \n1.positive\n2.negative\n3.neutral  here->\t"""))
        if(user=="positive"or user=="1"):
            positive()
        elif(user=="negative"or user=="2"):
            negative()
        elif(user=="neutral"or user=="3"):
            neutral()
        elif(user=="br"or user=="4"):
            break
        else:
            print("\nSorry but it is invalid input you can try again from below\n")
        j+=1
    print("there are ",429772-277612,"negative comments then positive comments")


except:
    print("some error occurred\U0001F605")
finally:
    print("thankyou for using our code, have a great day!!\U0001F601")



