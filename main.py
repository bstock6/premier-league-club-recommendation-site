from bakery import assert_equal
from drafter import *
from dataclasses import dataclass



hide_debug_information()
set_website_title("Premier League Club Recommender")
set_website_framed(False)
set_site_information(author = "Brayden Stockmaster", description= "A site meant for beginner soccer fans to get an idea of Premier League Clubs they may enjoy watching", sources= ["Premier League Rosters", "CISC 106 LLM" ], planning= ["Pick a Problem Document", "Planning Document"], links=["https://www.premierleague.com/en/players?competition=8&season=2026"])


@dataclass
class Player:
    """Store information about one player to watch.

    Args:
        name: The player's name.
        position: The player's listed playing position.
        number: The player's shirt number.
        club: The club the player represents.

    Returns:
        A Player object containing the supplied information.
    """
    name: str
    position: str
    number: int
    club: str


@dataclass
class State:
    """Store the user's answers and current recommendation.

    Args:
        playstyle: The user's preferred style of play.
        key_players: A list of Player objects for the recommended club.
        color: The user's preferred team color.
        fans: The user's preferred type of fanbase.
        size: The user's preferred club size.
        competitiveness: The user's preferred competitive level.
        questions_answered: The number of questions completed.
        recommendation: The name of the recommended club.

    Returns:
        A State object containing the website's current information.
    """
    playstyle: str
    key_players: list[Player]
    color: str
    fans: str
    size: str
    competitiveness: str
    questions_answered: int
    recommendation: str


# -----------------------------------------
# CONSTANT DATA
# -----------------------------------------

PLAYSTYLE_OPTIONS = [
    "Attacking (Focuses on scoring goals and creating chances.)",
    "Possession (Focuses on keeping the ball and building attacks.)",
    "Defensive (Focuses on preventing goals and limiting opponents.)",
    "Counter-attacking (Attacks quickly after winning the ball.)"
]

FAN_OPTIONS = [
    "Loud and passionate",
    "Global and large",
    "Community-focused"
]

SIZE_OPTIONS = ["Large", "Medium", "Small"]

COMPETITIVENESS_OPTIONS = [
    "Title contenders",
    "European qualification",
    "Mid-table stability",
    "Survival"
]

COLOR_OPTIONS = [
    "Red",
    "Blue",
    "White",
    "Black",
    "Yellow",
    "Claret and Blue",
    "Orange and Black",
    "Green",
    "Red and White",
    "Blue and White",
    "Black and White",
    "Red and Black",
    "Red and Blue"
]


# -----------------------------------------
# PLAYER DATABASE
# Three players from every club:
# one attacker, one winger, and one defender.
# -----------------------------------------

PLAYERS = [
    # Arsenal
    Player("Bukayo Saka", "Winger", 7, "Arsenal"),
    Player("Martin Odegaard", "Center Attacking Midfielder", 8, "Arsenal"),
    Player("William Saliba", "Defender", 2, "Arsenal"),

    # Aston Villa
    Player("Nicolas Jackson", "Attacker", 11, "Aston Villa"),
    Player("Alejandro Garnacho", "Winger", 17, "Aston Villa"),
    Player("Pau Torres", "Defender", 14, "Aston Villa"),

    # Bournemouth
    Player("Evanilson", "Attacker", 9, "Bournemouth"),
    Player("Rayan", "Winger", 37, "Bournemouth"),
    Player("Adrien Truffert", "Defender", 3, "Bournemouth"),

    # Brentford
    Player("Igor Thiago", "Attacker", 9, "Brentford"),
    Player("Kevin Schade", "Winger", 7, "Brentford"),
    Player("Nathan Collins", "Defender", 22, "Brentford"),

    # Brighton
    Player("Stefanos Tzimas", "Attacker", 9, "Brighton"),
    Player("Kaoru Mitoma", "Winger", 7, "Brighton"),
    Player("Lewis Dunk", "Defender", 5, "Brighton"),

    # Chelsea
    Player("Joao Pedro", "Attacker", 9, "Chelsea"),
    Player("Cole Palmer", "Winger/Attacking Midfielder", 10, "Chelsea"),
    Player("Levi Colwill", "Defender", 6, "Chelsea"),

    # Coventry City
    Player("Ellis Simms", "Attacker", 9, "Coventry City"),
    Player("Tatsuhiro Sakamoto", "Winger", 7, "Coventry City"),
    Player("Ethan Pinnock", "Defender", 2, "Coventry City"),

    # Crystal Palace
    Player("Jean-Philippe Mateta", "Attacker", 14, "Crystal Palace"),
    Player("Ismaila Sarr", "Winger/Attacking Midfielder", 7,
           "Crystal Palace"),
    Player("Tyrick Mitchell", "Defender", 3, "Crystal Palace"),

    # Everton
    Player("Thierno Barry", "Attacker", 11, "Everton"),
    Player("Jack Grealish", "Winger", 10, "Everton"),
    Player("Jarrad Branthwaite", "Defender", 4, "Everton"),

    # Fulham
    Player("Rodrigo Muniz", "Attacker", 9, "Fulham"),
    Player("Kevin", "Winger", 11, "Fulham"),
    Player("Calvin Bassey", "Defender", 3, "Fulham"),

    # Hull City
    Player("Oliver McBurnie", "Attacker", 9, "Hull City"),
    Player("Mohamed Belloumi", "Winger", 10, "Hull City"),
    Player("Charlie Hughes", "Defender", 4, "Hull City"),

    # Ipswich Town
    Player("Zian Flemming", "Attacker", 9, "Ipswich Town"),
    Player("Abdul Fatawu", "Winger", 7, "Ipswich Town"),
    Player("Leif Davis", "Defender", 3, "Ipswich Town"),

    # Leeds United
    Player("Dominic Calvert-Lewin", "Attacker", 9, "Leeds United"),
    Player("Daniel James", "Winger", 7, "Leeds United"),
    Player("Joe Rodon", "Defender", 6, "Leeds United"),

    # Liverpool
    Player("Alexander Isak", "Attacker", 9, "Liverpool"),
    Player("Bradley Barcola", "Winger", 29, "Liverpool"),
    Player("Virgil van Dijk", "Defender", 4, "Liverpool"),

    # Manchester City
    Player("Erling Haaland", "Attacker", 9, "Manchester City"),
    Player("Jeremy Doku", "Winger", 11, "Manchester City"),
    Player("Ruben Dias", "Defender", 3, "Manchester City"),

    # Manchester United
    Player("Benjamin Sesko", "Attacker", 30, "Manchester United"),
    Player("Bryan Mbeumo", "Winger", 19, "Manchester United"),
    Player("Matthijs de Ligt", "Defender", 4, "Manchester United"),

    # Newcastle United
    Player("Yoane Wissa", "Attacker", 9, "Newcastle United"),
    Player("Anthony Elanga", "Winger", 19, "Newcastle United"),
    Player("Sven Botman", "Defender", 4, "Newcastle United"),

    # Nottingham Forest
    Player("Chris Wood", "Attacker", 9, "Nottingham Forest"),
    Player("Callum Hudson-Odoi", "Winger", 7, "Nottingham Forest"),
    Player("Murillo", "Defender", 5, "Nottingham Forest"),

    # Sunderland
    Player("Brian Brobbey", "Attacker", 9, "Sunderland"),
    Player("Chemsdine Talbi", "Winger", 7, "Sunderland"),
    Player("Dan Ballard", "Defender", 5, "Sunderland"),

    # Tottenham Hotspur
    Player("Dominic Solanke", "Attacker", 19, "Tottenham Hotspur"),
    Player("Mohammed Kudus", "Winger", 20, "Tottenham Hotspur"),
    Player("Micky van de Ven", "Defender", 37, "Tottenham Hotspur")
]


# -----------------------------------------
# CLUB DATABASE
# -----------------------------------------

CLUBS = [
    {
        "name": "Arsenal",
        "playstyle": "Possession",
        "color": "Red",
        "fans": "Global and large",
        "size": "Large",
        "competitiveness": "Title contenders",
        "history": (
            "Arsenal are one of England's most successful clubs. "
            "Their most famous achievement was the 2003-04 "
            "Invincibles season, when they won the Premier League "
            "without losing a single match. They finished with "
            "26 wins and 12 draws. They have also won numerous "
            "FA Cups and league titles."
        )
    },
    {
        "name": "Aston Villa",
        "playstyle": "Counter-attacking",
        "color": "Claret and Blue",
        "fans": "Community-focused",
        "size": "Large",
        "competitiveness": "European qualification",
        "history": (
            "Aston Villa are one of England's oldest and most "
            "successful clubs. They won the European Cup in 1982 "
            "by defeating Bayern Munich 1-0 in the final. They "
            "have also won seven English league titles and "
            "multiple domestic trophies."
        )
    },
    {
        "name": "Bournemouth",
        "playstyle": "Attacking",
        "color": "Red and Black",
        "fans": "Community-focused",
        "size": "Small",
        "competitiveness": "Mid-table stability",
        "history": (
            "Bournemouth have experienced a remarkable rise "
            "through English football. They first reached the "
            "Premier League in 2015, after spending much of "
            "their history in the lower divisions. Their rise "
            "is considered one of the club's greatest achievements."
        )
    },
    {
        "name": "Brentford",
        "playstyle": "Counter-attacking",
        "color": "Red and White",
        "fans": "Community-focused",
        "size": "Small",
        "competitiveness": "Mid-table stability",
        "history": (
            "Brentford returned to the top division of English "
            "football in 2021 after a 74-year absence. They have "
            "become known for their use of statistics and data "
            "when recruiting players. Their promotion to the "
            "Premier League marked a major achievement for "
            "the West London club."
        )
    },
    {
        "name": "Brighton",
        "playstyle": "Possession",
        "color": "Blue and White",
        "fans": "Community-focused",
        "size": "Medium",
        "competitiveness": "European qualification",
        "history": (
            "Brighton spent many years outside the top division "
            "before reaching the Premier League in 2017. They "
            "qualified for European competition for the first "
            "time in their history in 2023 after finishing sixth "
            "in the Premier League. They are recognized for "
            "their player development and recruitment."
        )
    },
    {
        "name": "Chelsea",
        "playstyle": "Possession",
        "color": "Blue",
        "fans": "Global and large",
        "size": "Large",
        "competitiveness": "Title contenders",
        "history": (
            "Chelsea have become one of England's most successful "
            "clubs in the modern era. They won their first "
            "Champions League title in 2012 by defeating Bayern "
            "Munich on penalties. They won the competition again "
            "in 2021. They have also won multiple Premier League "
            "titles and FA Cups."
        )
    },
    {
        "name": "Coventry City",
        "playstyle": "Attacking",
        "color": "Blue",
        "fans": "Community-focused",
        "size": "Medium",
        "competitiveness": "Survival",
        "history": (
            "Coventry City's most famous achievement came in "
            "1987 when they won their first FA Cup. They defeated "
            "Tottenham Hotspur 3-2 in a memorable final. The "
            "club has experienced promotion and relegation "
            "throughout its history."
        )
    },
    {
        "name": "Crystal Palace",
        "playstyle": "Counter-attacking",
        "color": "Red and Blue",
        "fans": "Loud and passionate",
        "size": "Medium",
        "competitiveness": "Mid-table stability",
        "history": (
            "Crystal Palace have a long history in English "
            "football and are known for their passionate "
            "supporters. They reached the FA Cup final in "
            "both 1990 and 2016, although they finished as "
            "runners-up on both occasions. Their home ground "
            "is Selhurst Park in South London."
        )
    },
    {
        "name": "Everton",
        "playstyle": "Defensive",
        "color": "Blue",
        "fans": "Loud and passionate",
        "size": "Large",
        "competitiveness": "Mid-table stability",
        "history": (
            "Everton are one of England's most historic football "
            "clubs. They have won nine English top-flight league "
            "titles and five FA Cups. Their most successful "
            "modern period included league titles in 1985 and "
            "1987, along with the European Cup Winners' Cup "
            "in 1985."
        )
    },
    {
        "name": "Fulham",
        "playstyle": "Possession",
        "color": "White",
        "fans": "Community-focused",
        "size": "Medium",
        "competitiveness": "Mid-table stability",
        "history": (
            "Fulham are the oldest professional football club "
            "in London. They have played at Craven Cottage since "
            "1896. One of their greatest achievements came in "
            "2010 when they reached the Europa League final, "
            "defeating several major European clubs along the way."
        )
    },
    {
        "name": "Hull City",
        "playstyle": "Counter-attacking",
        "color": "Orange and Black",
        "fans": "Community-focused",
        "size": "Small",
        "competitiveness": "Survival",
        "history": (
            "Hull City first reached the Premier League in 2008. "
            "They made history in 2014 by reaching their first "
            "FA Cup final, where they narrowly lost 3-2 to Arsenal "
            "after extra time. The club represents the city "
            "of Hull in East Yorkshire."
        )
    },
    {
        "name": "Ipswich Town",
        "playstyle": "Attacking",
        "color": "Blue",
        "fans": "Community-focused",
        "size": "Small",
        "competitiveness": "Survival",
        "history": (
            "Ipswich Town won their first and only English "
            "top-flight league title in 1962, shortly after "
            "being promoted to the First Division. They also "
            "won the UEFA Cup in 1981 under manager Bobby Robson. "
            "These achievements remain some of the greatest "
            "moments in the club's history."
        )
    },
    {
        "name": "Leeds United",
        "playstyle": "Attacking",
        "color": "White",
        "fans": "Loud and passionate",
        "size": "Large",
        "competitiveness": "Mid-table stability",
        "history": (
            "Leeds United have won three English league titles "
            "and have a history of competing at the highest "
            "level. They reached the European Cup final in 1975 "
            "and won the Inter-Cities Fairs Cup in 1968 and 1971. "
            "Their passionate supporters make them one of "
            "England's most recognizable clubs."
        )
    },
    {
        "name": "Liverpool",
        "playstyle": "Attacking",
        "color": "Red",
        "fans": "Loud and passionate",
        "size": "Large",
        "competitiveness": "Title contenders",
        "history": (
            "Liverpool are one of the most successful clubs in "
            "English and European football. They have won 20 "
            "English league titles and six European Cups or "
            "Champions League titles. Their famous 2005 Champions "
            "League comeback against AC Milan in Istanbul is "
            "considered one of football's greatest finals."
        )
    },
    {
        "name": "Manchester City",
        "playstyle": "Possession",
        "color": "Blue",
        "fans": "Global and large",
        "size": "Large",
        "competitiveness": "Title contenders",
        "history": (
            "Manchester City have become one of the dominant "
            "clubs in modern football. In 2023, they completed "
            "the historic continental treble by winning the "
            "Premier League, FA Cup, and Champions League in "
            "the same season. In 2024, they became the first "
            "English men's team to win four consecutive "
            "top-flight league titles."
        )
    },
    {
        "name": "Manchester United",
        "playstyle": "Attacking",
        "color": "Red",
        "fans": "Global and large",
        "size": "Large",
        "competitiveness": "European qualification",
        "history": (
            "Manchester United are one of the most successful "
            "clubs in English football, with 20 league titles. "
            "Their famous 1999 season saw them win the Premier "
            "League, FA Cup, and Champions League to complete "
            "the historic treble. They are also remembered for "
            "legendary players such as George Best, Eric Cantona, "
            "and Cristiano Ronaldo."
        )
    },
    {
        "name": "Newcastle United",
        "playstyle": "Counter-attacking",
        "color": "Black and White",
        "fans": "Loud and passionate",
        "size": "Large",
        "competitiveness": "European qualification",
        "history": (
            "Newcastle United have a proud history and one of "
            "the most passionate fanbases in England. They have "
            "won four English league titles and six FA Cups. "
            "Their last league championship came in 1927, "
            "making a return to the top of English football "
            "a long-standing ambition."
        )
    },
    {
        "name": "Nottingham Forest",
        "playstyle": "Defensive",
        "color": "Red",
        "fans": "Loud and passionate",
        "size": "Medium",
        "competitiveness": "Mid-table stability",
        "history": (
            "Nottingham Forest achieved one of football's most "
            "remarkable accomplishments under manager Brian "
            "Clough. After winning the English league title in "
            "1978, they won the European Cup in both 1979 and "
            "1980. They remain one of the few English clubs to "
            "have won Europe's biggest trophy multiple times."
        )
    },
    {
        "name": "Sunderland",
        "playstyle": "Counter-attacking",
        "color": "Red and White",
        "fans": "Loud and passionate",
        "size": "Medium",
        "competitiveness": "Survival",
        "history": (
            "Sunderland are one of England's historic football "
            "clubs, having won six English league championships. "
            "Their last league title came in 1936. They also "
            "won the FA Cup in 1973 after defeating Leeds United "
            "1-0 in one of the competition's famous upsets."
        )
    },
    {
        "name": "Tottenham Hotspur",
        "playstyle": "Attacking",
        "color": "White",
        "fans": "Global and large",
        "size": "Large",
        "competitiveness": "European qualification",
        "history": (
            "Tottenham Hotspur have a long history of success "
            "in English and European football. They became the "
            "first British club to win a major European trophy "
            "when they won the European Cup Winners' Cup in "
            "1963. They also won the first UEFA Cup in 1972 "
            "and have won multiple FA Cups."
        )
    }
]


# -----------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------

def player_category(player: Player) -> str:
    """Group a player's position into one of three display roles.

    Args:
        player: A Player instance from the player database.

    Returns:
        "Attacker", "Winger", or "Defender" for recognized positions.
        "Other" is returned when the position does not fit a category.
    """
    if player.position == "Center Attacking Midfielder":
        return "Attacker"
    elif player.position == "Winger/Attacking Midfielder":
        return "Winger"
    elif player.position in ["Attacker", "Winger", "Defender"]:
        return player.position
    else:
        return "Other"


def playstyle_label(playstyle: str) -> str:
    """Return the full option text for a saved playstyle.

    Args:
        playstyle: The short playstyle name saved in State.

    Returns:
        The matching option with its explanation, or the first option
        if no match is found.
    """
    for option in PLAYSTYLE_OPTIONS:
        if option.startswith(playstyle + " "):
            return option
    return PLAYSTYLE_OPTIONS[0]


def recommend_club(state: State) -> str:
    """Choose the club with the highest preference score.

    Playstyle, size, and competitiveness are worth three points each.
    Fanbase is worth two points. Color is used only to break a top-score
    tie.

    Args:
        state: The user's saved questionnaire answers.

    Returns:
        The name of the highest-scoring club.
    """
    scores = []
    best_score = -1

    for club in CLUBS:
        score = 0

        if club["playstyle"] == state.playstyle:
            score += 3

        if club["size"] == state.size:
            score += 3

        if club["competitiveness"] == state.competitiveness:
            score += 3

        if club["fans"] == state.fans:
            score += 2

        scores.append([club, score])

        if score > best_score:
            best_score = score

    best_club = ""
    color_match_found = False

    for result in scores:
        club = result[0]
        score = result[1]

        if score == best_score:
            if best_club == "":
                best_club = club["name"]

            if club["color"] == state.color:
                if not color_match_found:
                    best_club = club["name"]
                    color_match_found = True

    return best_club


def find_club(club_name: str) -> dict:
    """Find a club's information in the club database.

    Args:
        club_name: The exact name of the club to find.

    Returns:
        The matching club dictionary, or the first club as a fallback
        when the name is not found.
    """
    for club in CLUBS:
        if club["name"] == club_name:
            return club

    return CLUBS[0]


def load_key_players(state: State) -> None:
    """Replace the saved player list with players from the recommendation.

    Args:
        state: The state whose key_players list will be updated.

    Returns:
        None. The function changes state.key_players directly.
    """
    state.key_players = []

    for player in PLAYERS:
        if player.club == state.recommendation:
            state.key_players.append(player)


# -----------------------------------------
# HOME PAGE
# -----------------------------------------

@route
def index(state: State) -> Page:
    """Display the welcome page.

    Args:
        state: The current website state.

    Returns:
        A Drafter Page containing the welcome message and start button.
    """
    return Page(state, [
        Header("Premier League Club Drafter"),
        "Not sure which Premier League club to support?",
        "Answer five soccer-related questions to discover "
        "which club best matches your preferences.",
        Button("Start Finding My Club", "playstyle")
    ])


# -----------------------------------------
# QUESTION 1: PLAYSTYLE
# -----------------------------------------

@route
def playstyle(state: State) -> Page:
    """Display the first question about preferred playing style.

    Args:
        state: The current website state, used to show the saved answer.

    Returns:
        A Drafter Page containing the playstyle selection.
    """
    return Page(state, [
        Header("Question 1: Playstyle"),
        "What type of soccer do you enjoy watching?",
        SelectBox(
            "choice",
            PLAYSTYLE_OPTIONS,
            playstyle_label(state.playstyle)
        ),
        Button("Continue", "save_playstyle")
    ])


@route
def save_playstyle(state: State, choice: str) -> Page:
    """Save the selected playstyle and continue to the fanbase question.

    Args:
        state: The current website state to update.
        choice: The selected playstyle option, including its explanation.

    Returns:
        The fanbase question page.
    """
    state.playstyle = choice.split(" (")[0]
    state.questions_answered += 1
    return fanbase(state)


# -----------------------------------------
# QUESTION 2: FANBASE
# -----------------------------------------

@route
def fanbase(state: State) -> Page:
    """Display the question about preferred supporters.

    Args:
        state: The current website state, used to show the saved answer.

    Returns:
        A Drafter Page containing the fanbase selection.
    """
    return Page(state, [
        Header("Question 2: Fanbase"),
        "What kind of supporters would you prefer?",
        SelectBox("choice", FAN_OPTIONS, state.fans),
        Button("Continue", "save_fanbase")
    ])


@route
def save_fanbase(state: State, choice: str) -> Page:
    """Save the fanbase preference and continue to the club-size question.

    Args:
        state: The current website state to update.
        choice: The selected fanbase preference.

    Returns:
        The club-size question page.
    """
    state.fans = choice
    state.questions_answered += 1
    return club_size(state)


# -----------------------------------------
# QUESTION 3: CLUB SIZE
# -----------------------------------------

@route
def club_size(state: State) -> Page:
    """Display the question about preferred club size.

    Args:
        state: The current website state, used to show the saved answer.

    Returns:
        A Drafter Page containing the club-size selection.
    """
    return Page(state, [
        Header("Question 3: Club Size"),
        "Would you prefer a large, medium, or small club?",
        SelectBox("choice", SIZE_OPTIONS, state.size),
        Button("Continue", "save_size")
    ])


@route
def save_size(state: State, choice: str) -> Page:
    """Save the club-size preference and continue to competitiveness.

    Args:
        state: The current website state to update.
        choice: The selected club size.

    Returns:
        The competitiveness question page.
    """
    state.size = choice
    state.questions_answered += 1
    return competitiveness(state)


# -----------------------------------------
# QUESTION 4: COMPETITIVENESS
# -----------------------------------------

@route
def competitiveness(state: State) -> Page:
    """Display the question about the club's competitive level.

    Args:
        state: The current website state, used to show the saved answer.

    Returns:
        A Drafter Page containing the competitiveness selection.
    """
    return Page(state, [
        Header("Question 4: Competitiveness"),
        "What level of success are you looking for?",
        SelectBox(
            "choice",
            COMPETITIVENESS_OPTIONS,
            state.competitiveness
        ),
        Button("Continue", "save_competitiveness")
    ])


@route
def save_competitiveness(state: State, choice: str) -> Page:
    """Save the competitiveness preference and continue to team colors.

    Args:
        state: The current website state to update.
        choice: The selected competitiveness level.

    Returns:
        The team-color question page.
    """
    state.competitiveness = choice
    state.questions_answered += 1
    return team_colors(state)


# -----------------------------------------
# QUESTION 5: TEAM COLORS
# -----------------------------------------

@route
def team_colors(state: State) -> Page:
    """Display the final question about preferred team colors.

    Args:
        state: The current website state, used to show the saved answer.

    Returns:
        A Drafter Page containing the team-color selection.
    """
    return Page(state, [
        Header("Question 5: Team Colors"),
        "Which team color do you prefer?",
        "Color is only used to separate clubs with matching scores.",
        SelectBox("choice", COLOR_OPTIONS, state.color),
        Button("Finish Questions", "save_color")
    ])


@route
def save_color(state: State, choice: str) -> Page:
    """Save the final answer and display questionnaire progress.

    Args:
        state: The current website state to update.
        choice: The selected team color.

    Returns:
        The questionnaire completion page.
    """
    state.color = choice
    state.questions_answered += 1
    return questions_remaining(state)


# -----------------------------------------
# QUESTIONNAIRE PROGRESS
# -----------------------------------------

@route
def questions_remaining(state: State) -> Page:
    """Display how many questionnaire questions were answered.

    Args:
        state: The current website state containing the answer count.

    Returns:
        A Drafter Page showing completed and remaining question counts.
    """
    remaining = 5 - state.questions_answered

    return Page(state, [
        Header("Questionnaire Complete!"),
        "You answered " + str(state.questions_answered) +
        " out of 5 questions.",
        "Questions remaining: " + str(remaining),
        Button("Find My Club", "recommendation")
    ])


# -----------------------------------------
# RECOMMENDATION PAGE
# -----------------------------------------

@route
def recommendation(state: State) -> Page:
    """Calculate the recommended club and display its featured players.

    Args:
        state: The current website state containing user preferences.

    Returns:
        A Drafter Page showing the recommended club and player list.
    """
    state.recommendation = recommend_club(state)
    load_key_players(state)

    page_contents = [
        Header("Your Premier League Club Is..."),
        Header(state.recommendation),
        "Based on your answers, this club is your best match!",
        Header("Three Players to Watch")
    ]

    for player in state.key_players:
        description = (
            player_category(player) + ": " + player.name +
            " (Number " + str(player.number) + ")"
        )
        page_contents.append(description + "\n")

    page_contents.append(
        Button("Learn About Your Club", "club_information")
    )
    page_contents.append(Button("See Club History", "history"))
    page_contents.append(Button("Start Over", "restart"))

    return Page(state, page_contents)


# -----------------------------------------
# CLUB INFORMATION PAGE
# -----------------------------------------

@route
def club_information(state: State) -> Page:
    """Display the recommended club's main characteristics.

    Args:
        state: The current website state containing the recommendation
            and featured players.

    Returns:
        A Drafter Page listing the club's attributes and players.
    """
    club = find_club(state.recommendation)

    page_contents = [
        Header(state.recommendation),
        "Playing Style: " + club["playstyle"] + "\n",
        "Team Colors: " + club["color"] + "\n",
        "Fanbase: " + club["fans"] + "\n",
        "Club Size: " + club["size"] + "\n",
        "Competitiveness: " + club["competitiveness"] + "\n",
        Header("Players to Watch")
    ]

    for player in state.key_players:
        description = (
            player_category(player) + ": " + player.name +
            " (#" + str(player.number) + ")"
        )
        page_contents.append(description + "\n")

    page_contents.append(Button("See Club History", "history"))
    page_contents.append(Button("Start Over", "restart"))

    return Page(state, page_contents)


# -----------------------------------------
# CLUB HISTORY PAGE
# -----------------------------------------

@route
def history(state: State) -> Page:
    """Display the saved history description for the recommended club.

    Args:
        state: The current website state containing the recommendation.

    Returns:
        A Drafter Page containing the club history and navigation buttons.
    """
    club = find_club(state.recommendation)

    return Page(state, [
        Header("Club History: " + state.recommendation),
        club["history"],
        Button("Back to Club Information", "club_information"),
        Button("Start Over", "restart")
    ])


# -----------------------------------------
# RESTART
# -----------------------------------------

@route
def restart(state: State) -> Page:
    """Create a fresh state and return the user to the welcome page.

    Args:
        state: The current website state. It is not changed.

    Returns:
        The welcome page using a new State with default answers.
    """
    new_state = State(
        "Attacking",
        [],
        "Red",
        "Loud and passionate",
        "Large",
        "Title contenders",
        0,
        ""
    )

    return index(new_state)


# -----------------------------------------
# UNIT TESTS
# -----------------------------------------

def test_club_database() -> None:
    """Test the number of clubs and player categories in the database.

    Args:
        None.

    Returns:
        None. Assertions raise an error if the database is inconsistent.
    """
    assert_equal(len(CLUBS), 20)
    assert_equal(len(PLAYERS), 60)

    for club in CLUBS:
        assert_equal(club["color"] in COLOR_OPTIONS, True)

        player_count = 0
        attacker_count = 0
        winger_count = 0
        defender_count = 0

        for player in PLAYERS:
            if player.club == club["name"]:
                player_count += 1

                category = player_category(player)
                if category == "Attacker":
                    attacker_count += 1
                elif category == "Winger":
                    winger_count += 1
                elif category == "Defender":
                    defender_count += 1

        assert_equal(player_count, 3)
        assert_equal(attacker_count, 1)
        assert_equal(winger_count, 1)
        assert_equal(defender_count, 1)


def test_recommendation_color_tiebreaker() -> None:
    """Test that color changes the result only between tied clubs.

    Args:
        None.

    Returns:
        None. Assertions raise an error if color overrides the main score.
    """
    red_state = State(
        "Attacking", [], "Red", "Loud and passionate",
        "Large", "European qualification", 5, ""
    )

    white_state = State(
        "Attacking", [], "White", "Loud and passionate",
        "Large", "European qualification", 5, ""
    )

    assert_equal(recommend_club(red_state), "Manchester United")
    assert_equal(recommend_club(white_state), "Tottenham Hotspur")


def test_playstyle_label() -> None:
    """Test matching and fallback behavior for playstyle descriptions.

    Args:
        None.

    Returns:
        None. Assertions raise an error if a label is incorrect.
    """
    assert_equal(
        playstyle_label("Possession"),
        PLAYSTYLE_OPTIONS[1]
    )
    assert_equal(
        playstyle_label("Unknown"),
        PLAYSTYLE_OPTIONS[0]
    )


def test_find_club() -> None:
    """Test club lookup for a valid name and an unknown name.

    Args:
        None.

    Returns:
        None. Assertions raise an error if lookup behavior is incorrect.
    """
    assert_equal(find_club("Arsenal")["name"], "Arsenal")
    assert_equal(
        find_club("Unknown Club")["name"],
        CLUBS[0]["name"]
    )


def test_load_key_players() -> None:
    """Test that only players from the recommended club are loaded.

    Args:
        None.

    Returns:
        None. Assertions raise an error if the player list is incorrect.
    """
    test_state = State(
        "Attacking", [], "Red", "Loud and passionate",
        "Large", "Title contenders", 0, "Arsenal"
    )

    load_key_players(test_state)

    assert_equal(len(test_state.key_players), 3)

    for player in test_state.key_players:
        assert_equal(player.club, "Arsenal")


def test_save_answers() -> None:
    """Test that each answer handler updates the appropriate state field.

    Args:
        None.

    Returns:
        None. Assertions raise an error if an answer is not saved.
    """
    test_state = State(
        "Attacking", [], "Red", "Loud and passionate",
        "Large", "Title contenders", 0, ""
    )

    save_playstyle(
        test_state,
        "Possession (Focuses on keeping the ball and building attacks.)"
    )

    assert_equal(test_state.playstyle, "Possession")
    assert_equal(test_state.questions_answered, 1)

    save_fanbase(test_state, "Community-focused")

    assert_equal(test_state.fans, "Community-focused")
    assert_equal(test_state.questions_answered, 2)

    save_size(test_state, "Small")

    assert_equal(test_state.size, "Small")
    assert_equal(test_state.questions_answered, 3)

    save_competitiveness(test_state, "Survival")

    assert_equal(test_state.competitiveness, "Survival")
    assert_equal(test_state.questions_answered, 4)

    save_color(test_state, "Blue")

    assert_equal(test_state.color, "Blue")
    assert_equal(test_state.questions_answered, 5)


def test_recommendation_route() -> None:
    """Test that the recommendation route saves a club and its players.

    Args:
        None.

    Returns:
        None. Assertions raise an error if recommendation state is missing.
    """
    test_state = State(
        "Possession", [], "Blue", "Global and large",
        "Large", "Title contenders", 5, ""
    )

    recommendation(test_state)

    assert_equal(test_state.recommendation, "Chelsea")
    assert_equal(len(test_state.key_players), 3)


def test_player_category() -> None:
    """Test the conversion of listed positions into player categories.

    Args:
        None.

    Returns:
        None. Assertions raise an error if a category is incorrect.
    """
    assert_equal(
        player_category(
            Player("Test", "Center Attacking Midfielder", 10, "Test Club")
        ),
        "Attacker"
    )

    assert_equal(
        player_category(
            Player("Test", "Winger/Attacking Midfielder", 7, "Test Club")
        ),
        "Winger"
    )

    assert_equal(
        player_category(
            Player("Test", "Defender", 4, "Test Club")
        ),
        "Defender"
    )

    assert_equal(
        player_category(
            Player("Test", "Goalkeeper", 1, "Test Club")
        ),
        "Other"
    )


# -----------------------------------------
# WEBSITE INFORMATION
# -----------------------------------------




# -----------------------------------------
# RUN UNIT TESTS
# -----------------------------------------

test_club_database()
test_recommendation_color_tiebreaker()
test_playstyle_label()
test_find_club()
test_load_key_players()
test_player_category()
test_save_answers()
test_recommendation_route()


# -----------------------------------------
# STARTING STATE
# -----------------------------------------

start_server(State(
    "Attacking",
    [],
    "Red",
    "Loud and passionate",
    "Large",
    "Title contenders",
    0,
    ""
))
