def game_specs(key):
    return " ".join(specs[key].split())


specs = dict(

NumSeq_game_specifications = """
NumSeq Scramble is a strategic board game where players aim to form the longest
sequences of the same digit on a 15x15 grid to score points. Each player starts
with 7 number tiles, drawing from a bag, and takes turns placing tiles to build
or extend sequences horizontally or vertically. Valid moves must connect to
existing sequences, and players draw new tiles to maintain 7 in hand. Points
are awarded based on sequence length, with bonuses for special tiles and
multiple sequences in one turn. The game includes wild tiles, combo bonuses,
and blocking strategies. It ends when no more valid moves are possible, and the
player with the highest score wins. Variations include timed turns, team play,
and advanced modes. The game promotes numerical recognition, strategic
thinking, and problem-solving skills, blending the familiar Scrabble format
with numerical challenges.
""",

Wordsum_game_specifications = """
Players start with a 9x9 blank grid similar to Sudoku, where each square can
hold a letter or number tile. The objective is to fill the grid with valid
words horizontally and vertically, while each row and column must also satisfy
numerical constraints like in Sudoku or Calcudoku. Players strategically place
tiles (letters A-Z and numbers 1-9) to form words and meet numerical
requirements without repetition. Points are awarded for word complexity and
meeting numerical constraints, advancing players to more challenging levels.
Special tiles and numerical modifiers, along with time-based or limited-move
challenges, add strategic depth to the game.
""",

Boggle_game_specifications = """
Players start with a 9x9 grid, where each square has a letter.
Player could choose a square and a direction (up, down, left, right) to form a word.
The word must be at least 3 letters long.
There will be one solution that every letter in the grid is used exactly once.
""",

LexiMath_game_specifications = """
Game Title: LexiMath Concept: LexiMath combines the word-building mechanics of
popular word games with the numerical challenge of mathematical puzzles.
Players strategically place tiles on a grid to form words horizontally and
vertically while ensuring numbers in the grid satisfy mathematical equations.
Mechanics: Grid Formation: Players work on a grid divided into squares where
each square can hold either a letter tile (A-Z) or a number tile (1-9).
Objective: Form words across the grid horizontally and vertically, similar to
word games like Scrabble. Ensure numbers in the grid contribute to solving
mathematical equations presented in the puzzle. Tile Placement: Players have
tiles containing both letters and numbers. Place these tiles strategically to
form words and satisfy mathematical equations simultaneously. Mathematical
Equations: Solve equations (e.g., addition, subtraction, multiplication,
division) using numbers placed in the grid. Numbers must satisfy both row and
column numerical constraints, similar to Sudoku. Why Play LexiMath? LexiMath
offers a unique blend of linguistic creativity and mathematical logic. It
challenges players to think strategically about both forming words and solving
mathematical equations within a single grid-based puzzle format.
""",

Word2048_game_specifications = """
Word2048 merges the sliding tile mechanics of 2048 with the word-building
creativity of Scrabble. Players slide letter tiles on a grid to form words,
combining identical letters to create higher-value words. The grid consists of
cells containing letter tiles (A-Z), which can be slid in four directions to
merge identical letters and form longer words. The objective is to create words
horizontally or vertically, earning points based on word length and complexity.
Merging two identical letter tiles advances the tile to the next alphabetical
letter. Points are awarded as players form words, and new tiles appear to
challenge them further. Strategic tile movements maximize word formation while
avoiding a full grid. Special word lengths or themes yield bonus points or
unlock special tiles for strategic advantages. Word2048 offers a dynamic
gameplay experience, blending linguistic skills and spatial reasoning for fans
of both word and puzzle games.
""",

Wordle_game_specifications = """
The client envisions a Wordle-inspired game where the target word can vary between 
3 to 5 letters. Players will have up to 10 guesses to identify the correct word. 
To aid players, an alphabet chart will be provided, utilizing color-coded indicators: 
grey for unseen letters, red for incorrect letters, green for correct letters in the 
right position, and yellow for correct letters in the wrong position. The game aims 
to enhance the typical Wordle experience while maintaining a similar core mechanic, 
adding a twist with variable word lengths. No additional features or mechanics 
such as themed word lists, daily challenges, or power-ups have been specified, but 
these can be considered in future conversations to enrich the player experience.
""",

Tictactoe_game_specifications = """
The client is seeking an HTML5-based Tic Tac Toe game with a comprehensive user interface 
that includes a welcome screen, menu buttons, game over screen, and a proper scoring mechanism. 
Specifically, the requirements are: 1. **Welcome Screen**: An initial screen that welcomes 
the user and includes a "Play" button to start the game. 2. **Game Board**: A 3x3 grid where 
players take turns to place their marks (X and O). The game board should be visually appealing 
and clearly indicate the current state of the game. 3. **Game Functions**: - **Player Turns**: 
Alternation between two players (Player 1 as X and Player 2 as O). - **Win Checking**: The 
ability to recognize and declare a winning condition when a player gets three of their marks 
in a row, column, or diagonal. - **Draw Condition**: Recognize and declare a draw if all grid 
squares are filled without a winner. 4. **Scoring Mechanism**: A scoreboard that keeps track 
of the number of wins for each player. 5. **Game Over Screen**: Display the winner or a draw 
message when the game ends. This should be followed by an option to reset the game or return 
to the main menu. 6. **Reset Functionality**: Ability to reset the game board for a new game 
while retaining the score. 7. **Main Menu**: The option to quit or restart the game from the 
main menu. The implementation should be responsive and user-friendly, encouraging engaging 
gameplay through intuitive design. The proposed technology stack includes HTML for structure, 
CSS for styling, and JavaScript for functionality to ensure an immersive and interactive gaming 
experience.
""",

Pure2048 = """
2048 Game Design Document
Game Concept and Vision

Overview:
2048 is a classic single-player sliding block puzzle game. The objective is to merge tiles with the same numbers to create the highest possible number, ultimately aiming to achieve the 2048 tile. The game ends when no more moves are possible, either because the player has created the 2048 tile (winning) or the board is full and no merges are available (losing).

Genre: Puzzle

Theme: Numerical Merging

Primary Objectives:

    Combine tiles to reach the 2048 tile.
    Keep playing to achieve even higher scores.

User Interface (UI)

Design and Layout:

    Main Menu:
        Play Button: Starts a new game.
        Reset Button: Resets the current game.
        Score Display: Shows current score.
        Best Score Display: Shows the highest score achieved.
        Instructions Button: Opens a popup with game rules and controls.

    In-Game UI:
        4x4 Grid: Displays game tiles.
        Score Display: In the top-right corner, dynamically updates as the game progresses.
        Restart Button: To restart the game at any point.
        Background: Simple, clean design with a focus on the grid to avoid distraction.

Visual Style and Aesthetic:

    Clean and minimalistic design.
    Soft colors for background and grid.
    Bright, distinguishable colors for tiles, with each unique number represented by a different color.

User Input Mechanisms

Interaction Methods:

    Control Scheme:
        Keyboard:
            Up Arrow: Moves tiles up.
            Down Arrow: Moves tiles down.
            Left Arrow: Moves tiles left.
            Right Arrow: Moves tiles right.
        Mouse/Tap (for UI only): Clicking buttons like 'Restart' or navigating the menu.

Game Logic

Core Gameplay Mechanics:

    Tile Movement:
        Pressing any arrow key slides all tiles in the direction of the arrow.
        Tiles combine if they collide with another tile of the same number, forming a single tile with a value equal to their sum.
        After each move, a new tile (2 or 4) appears in a random empty spot on the board.

    Game Progression:
        Score increases based on the value of the tiles merged.
        The game continues until a 2048 tile is created or no valid moves remain.

Win/Loss Conditions:

    Winning Condition:
        Form a tile with the number 2048.
    Losing Condition:
        The grid is full, and no tiles can be merged.

Scoring:

    Scores accumulate based on merging tiles. Each merge adds to the score the combined value of the tiles.

Rules

Objective:
Combine numbered tiles to reach 2048 while maximizing the score.

Controls:

    Keyboard:
        Up Arrow: Moves tiles up.
        Down Arrow: Moves tiles down.
        Left Arrow: Moves tiles left.
        Right Arrow: Moves tiles right.

Actions:

    Move Tiles:
        Directional arrow keys to slide tiles.
    Combine Tiles:
        Same-number tiles merge to form a tile with a combined value.

Action Restrictions:

    Tiles only move in the direction of the arrow key and only merge if possible.
    New tiles (2 or 4) are generated in empty spaces after each move.

In-Game Assets and Content

Necessary Assets:

    Characters: Not applicable.
    Items:
        Numbered Tiles: 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048 (and higher).
    Environments:
        4x4 Grid Background.

Sound Effects and Music:

    Sound Effects:
        Tile Merging Sound.
        Tile Placement Sound.
        Victory Sound for achieving 2048.
    Background Music:
        Light and unobtrusive looping track.

Additional Components

Unique Mechanics:

    None beyond the original mechanics.

Implementation Considerations

Challenges:

    Ensuring smooth tile movement and proper merging mechanics.
    Balancing the randomness of new tile placement to maintain fairness.
    Creating an engaging and responsive UI that works seamlessly across different devices.

Development Focus:

    High attention to the responsiveness of tile movements and merges for a smooth user experience.
    Ensuring all animations are fluid to keep the game visually appealing and engaging.
    Consistent updating of scores and game state.

With these detailed guidelines, you should have a clear and comprehensive design plan for creating your version of the classic 2048 game. Good luck with your development!
""",

word_tetris = """
Game Concept Writeup: Letter Tetris
Game Concept and Vision
Summary

Letter Tetris is a unique twist on the classic Tetris game where instead of shapes, individual letters fall down into a 10x20 grid. The primary objective is to form valid horizontal words to score points. Words are scored based on the letters they contain, with more common letters giving fewer points and less common letters giving more points, similar to the Scrabble scoring system. The game ends when the stack of letters reaches the top of the screen.
Setting and Theme

    Genre: Puzzle
    Theme: Retro, minimalist
    Visual Style: Simple and retro with a focus on functionality. The background, letters, and the game's interface will have a minimalist aesthetic reminiscent of early video games.

Primary Objectives

    Form horizontal words by moving and placing falling letters.
    Achieve the highest score possible by strategically placing letters to maximize word value.
    Avoid stacking letters to the top of the screen to keep the game going.

User Interface (UI)
Design and Layout

    Main Menu:
        Start Game
        How to Play / Instructions
        High Scores
        Settings (Volume Control)
        Exit

    Game Screen:
        Grid: 10x20 cell layout
        HUD: Displays current score, upcoming letter, and possibly number of words formed
        Control UI: On-screen controls are omitted to maintain simplicity, as the game relies on keyboard input.

    Game Over Screen:
        Display final score
        Option to restart or return to the main menu

Visual Style

    Grid and Letters: Clean, block-style letters with clearly legible characters.
    Background: A plain, non-distracting color to emphasize the falling letters and grid.
    Fonts and Colors: Retro-styled fonts with high contrast colors for visibility and retro aesthetics.

User Input Mechanisms
Controls

    Keyboard:
        Left Arrow Key: Move letter block left
        Right Arrow Key: Move letter block right
        Down Arrow Key: Accelerate the descent of the letter block

Input Actions

    Moving Letters: User uses arrow keys to navigate the falling letter to its desired position.
    Placing Letters: Letters automatically place themselves when they hit the bottom of the grid or another letter.

Game Logic
Core Gameplay Mechanics

    Falling Letters: Letters fall from the top of the grid.
    Forming Words: Arrange falling letters to form horizontal words.
    Clearing Words: Once a valid word is formed, it is cleared from the grid, and the player scores points based on the Scrabble score for those letters.

Scoring System

    Points:
        Follows the Scrabble letter points:
            Common letters (e.g., E, A, I, O) = 1 point,
            Less common letters (e.g., K) = 5 points,
            Rare letters (e.g., Z, Q) = 10 points.
    Frequency: More common letters fall more frequently, while less common, high-point letters fall less frequently.
    Cumulative Score: The player’s total score is a cumulative sum of the points earned for each word formed.

End Conditions

    Game Over: Occurs when the stack of letters reaches the top of the grid.

Rules Menu
Objectives

    Primary Goal: Achieve the highest score by forming and clearing valid words.
    Victory Conditions: Continue playing and scoring until the stack reaches the top of the screen.

Controls

    Arrow Keys:
        Left: Move letter left
        Right: Move letter right
        Down: Speed up descent

Actions

    Move Left/Right: Position the falling letter.
    Accelerate Down: Speed up the letter's descent.
    Form Words: Align letters horizontally to create valid words based on a standard English dictionary.
    Clear Words: Valid words are removed from the grid, and the player scores points.

In-Game Assets and Content
Necessary Assets

    Letters: Stylized letter blocks from A-Z.
    Grid: 10x20 cell grid layout.
    HUD Elements: Score display, upcoming letter preview.
    Background Music: Chiptunes style music track that loops during gameplay.
    Fonts: Retro, pixelated font for UI and letters.

Content

    Dictionary: Standard English dictionary for word validation.
    Scoring Table: Points assigned per letter matching the Scrabble scoring system.

Additional Components
Unique Features

    Word Validation: Real-time checking of formed words against a dictionary.
    Letter Frequency: Algorithm to ensure correct frequency of letter appearance based on their commonality in the English language.

Implementation Considerations
Development Challenges

    Real-time Word Validation: Implementing an efficient algorithm to check for valid words as letters land.
    Letter Frequency: Balancing the appearance of letters to maintain game difficulty and player engagement.
    Smooth Controls: Ensuring smooth and responsive controls to allow precise placement of falling letters.

Design Focus Areas

    Gameplay Balance: Avoiding overwhelming the player with too many difficult-to-place letters while still challenging them.
    User Experience: Maintaining a simple, clean interface that doesn’t distract from the core gameplay.
    Music Integration: Making sure the background music enhances the ambiance without becoming monotonous.

With these considerations, you have a comprehensive writeup that will guide the complete development process of your Letter Tetris game. This framework covers all necessary elements to create an engaging and balanced puzzle game that stays true to your vision.
"""

)
