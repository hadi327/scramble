import random
import time
class WordScrambleGame:
    def __init__(self):
        self.score = 0
        self.rounds = 0
        self.hints_used = 0
        self.difficulty = 'medium'

        self.words = {
            'easy': [
                'cat', 'dog', 'sun', 'hat', 'run', 'big', 'red', 'cup',
                'map', 'pen', 'car', 'sky', 'tree', 'star', 'moon', 'fish',
                'bird', 'book', 'desk', 'lamp', 'rose', 'gold', 'love', 'hope'
            ],
            'medium': [
                'python', 'birthday', 'paris', 'vegas', 'memory',
                'gold', 'vintage', 'crystal', 'velvet', 'cinema', 'jazz',
                'piano', 'sunset', 'silver', 'diamond', 'charm', 'elegant',
                'garden', 'orchard', 'palace', 'mystery', 'harmony'
            ],
            'hard': [
                'champagne', 'boulevard', 'sophisticated', 'chandelier',
                'perfume', 'romance', 'fashion', 'velvet', 'cffa',
                'enchanting', 'memories', 'treasure', 'lavender', 'crystal',
                'euphoria', 'silhouette', 'nostalgia', 'serendipity'
            ]
        }
        self.special_words = [ 'paris', 'vegas', 'cffa', 'vintage', 'gold']
        for level in self.words:
            self.words[level].extend(self.special_words)

    def scramble_word(self, word):
        """Scramble the letters of a word"""
        letters = list(word)
        attempts = 0
        # Ensure word is actually scrambled
        while ''.join(letters) == word and attempts < 10:
            random.shuffle(letters)
            attempts += 1
        return ''.join(letters)

    def get_hint(self, word):
        """Provide a hint about the word"""
        hints = [
            f"📝 The word has {len(word)} letters",
            f"🔤 Starts with '{word[0]}'",
            f"🔤 Ends with '{word[-1]}'",
            f"📚 It's related to: {self.get_category(word)}",
            f"💡 Contains {len(set(word))} unique letters"
        ]
        return hints[self.hints_used % len(hints)]

    def get_category(self, word):
        """Get the category of a word"""
        categories = {
            '🌍 Place': ['paris', 'vegas', 'rome', 'london', 'venice', 'milan'],
            '🎨 Style': ['vintage', 'elegant', 'classic', 'modern', 'chic', 'bold'],
            '💎 Luxury': ['gold', 'silver', 'diamond', 'pearl', 'crystal', 'velvet'],
            '🎵 Music': ['jazz', 'piano', 'opera', 'symphony', 'melody', 'rhythm'],
            '💝 Special': ['cffa', 'dream', 'hope', 'love', 'light']
        }

        for category, words in categories.items():
            if word.lower() in words:
                return category
        return '✨ something special ✨'

    def choose_mode(self):
        """Display menu and get mode choice"""
        print("\n" + "=" * 50)
        print("🎯 WORD SCRAMBLE - ALL IN ONE 🎯")
        print("=" * 50)
        print("\n📌 Choose a mode:")
        print("1️⃣ Classic Mode - Just unscramble!")
        print("2️⃣ Pro Mode - With hints & difficulty")
        print("3️⃣ Timed Mode - Beat the clock!")
        print("4️⃣ Multiplayer - Challenge a friend")
        print("5️⃣ Custom Mode - Play with your own words")
        print("6️⃣ How to Play")
        print("7️⃣ Exit")

        while True:
            choice = input("\n👉 Enter your choice (1-7): ").strip()
            if choice in ['1', '2', '3', '4', '5', '6', '7']:
                return choice
            print("❌ Invalid choice. Please enter 1-7.")

    def play_classic(self):
        """Classic mode - simple scramble"""
        print("\n🎯 CLASSIC MODE - Just unscramble!")
        print("Type 'quit' to exit back to menu\n")

        score = 0
        rounds = 0

        while True:
            word = random.choice(self.words[self.difficulty])
            scrambled = self.scramble_word(word)
            rounds += 1

            print(f"🔀 Round {rounds}: {scrambled}")
            guess = input("Your guess: ").lower().strip()

            if guess == 'quit':
                print(f"\n📊 Score: {score}/{rounds - 1}")
                return

            if guess == word:
                print("✅ Correct! 🎉")
                score += 1
            else:
                print(f"❌ Wrong! It was: {word}")

            print(f"📊 Score: {score}/{rounds}\n")

    def play_pro_mode(self):
        """Pro mode with hints and difficulty"""
        print("\n🌟 PRO MODE - With hints & difficulty")
        print("Type 'hint' for help, 'quit' to exit\n")

        # Choose difficulty
        print("📊 Select Difficulty:")
        print("1. Easy 🟢")
        print("2. Medium 🟡")
        print("3. Hard 🔴")

        diff_choice = input("Enter 1, 2, or 3: ").strip()
        if diff_choice == '1':
            self.difficulty = 'easy'
        elif diff_choice == '3':
            self.difficulty = 'hard'
        else:
            self.difficulty = 'medium'

        print(f"\n✅ Playing on {self.difficulty.upper()} mode!\n")

        score = 0
        rounds = 0
        hints_available = 3

        while True:
            word = random.choice(self.words[self.difficulty])
            scrambled = self.scramble_word(word)
            rounds += 1

            print(f"\n🔄 Round {rounds}")
            print(f"🔀 Scrambled: {scrambled}")
            print(f"💡 Hints remaining: {hints_available}")

            while True:
                guess = input("Your guess: ").lower().strip()

                if guess == 'quit':
                    print(f"\n📊 Score: {score}/{rounds - 1}")
                    return

                if guess == 'hint':
                    if hints_available > 0:
                        hint = self.get_hint(word)
                        print(f"💡 {hint}")
                        hints_available -= 1
                        self.hints_used += 1
                    else:
                        print("❌ No more hints left!")
                    continue

                if guess == word:
                    print("✅ Correct! 🎉")
                    score += 1
                    break
                else:
                    print(f"❌ Wrong! Try again.")
                    print(f"💡 Hint: The word has {len(word)} letters")

    def play_timed_mode(self):
        """Timed mode with 30 seconds per word"""
        print("\n⏰ TIMED MODE - 30 seconds per word!")
        print("Type 'quit' to exit back to menu\n")

        score = 0
        rounds = 0

        while True:
            word = random.choice(self.words['medium'])
            scrambled = self.scramble_word(word)
            rounds += 1

            print(f"\n🔄 Round {rounds}")
            print(f"🔀 Scrambled: {scrambled}")
            print("⏱️  You have 30 seconds!")

            start_time = time.time()
            guess = input("Your guess: ").lower().strip()

            if guess == 'quit':
                print(f"\n📊 Score: {score}/{rounds - 1}")
                return

            elapsed = time.time() - start_time

            if elapsed > 30:
                print(f"⏰ Time's up! The word was: {word}")
            elif guess == word:
                time_taken = round(elapsed, 1)
                print(f"✅ Correct! 🎉 (Took {time_taken}s)")
                score += 1
            else:
                print(f"❌ Wrong! The word was: {word}")

            print(f"📊 Score: {score}/{rounds}")

    def play_multiplayer(self):
        """Two player mode"""
        print("\n👥 MULTIPLAYER MODE")
        print("Players take turns unscrambling words\n")

        scores = {'Player 1': 0, 'Player 2': 0}
        players = ['Player 1', 'Player 2']
        turn = 0

        print("📊 Select Difficulty for this game:")
        print("1. Easy 🟢")
        print("2. Medium 🟡")
        print("3. Hard 🔴")

        diff_choice = input("Enter 1, 2, or 3: ").strip()
        if diff_choice == '1':
            difficulty = 'easy'
        elif diff_choice == '3':
            difficulty = 'hard'
        else:
            difficulty = 'medium'

        rounds = int(input("How many rounds? (3-10): ") or "5")
        rounds = max(3, min(10, rounds))

        print(f"\n🎮 Playing {rounds} rounds on {difficulty.upper()} mode!\n")

        for round_num in range(1, rounds + 1):
            current_player = players[turn]
            print(f"\n🔄 Round {round_num} - {current_player}'s turn")

            word = random.choice(self.words[difficulty])
            scrambled = self.scramble_word(word)

            print(f"🔀 Scrambled: {scrambled}")
            guess = input("Your guess: ").lower().strip()

            if guess == 'quit':
                break

            if guess == word:
                print("✅ Correct! +1 point 🎉")
                scores[current_player] += 1
            else:
                print(f"❌ Wrong! The word was: {word}")

            print(f"📊 Scores: P1: {scores['Player 1']} | P2: {scores['Player 2']}")
            turn = 1 - turn  # Switch players

        # Show winner
        print("\n" + "=" * 50)
        print("🏆 GAME OVER!")
        print("=" * 50)
        p1, p2 = scores['Player 1'], scores['Player 2']

        if p1 > p2:
            print("👑 Player 1 WINS! 🎉")
        elif p2 > p1:
            print("👑 Player 2 WINS! 🎉")
        else:
            print("🤝 It's a tie!")

        print(f"📊 Final Score: Player 1: {p1} | Player 2: {p2}")

    def play_custom_mode(self):
        """Play with custom word list"""
        print("\n✨ CUSTOM MODE - Your own words!")
        print("Enter words separated by commas (or press Enter for default)\n")

        custom_input = input("Enter your words: ").strip()

        if custom_input:
            custom_words = [w.strip().lower() for w in custom_input.split(',')]
            self.words['custom'] = custom_words
            print(f"✅ Added {len(custom_words)} custom words!")
        else:
            self.words['custom'] = ['paris', 'vegas', 'cffa', 'vintage', 'gold']
            print("📖 Using default custom words!")

        print("\n🔀 Unscramble your custom words!")
        print("Type 'quit' to exit\n")

        score = 0
        rounds = 0

        while True:
            word = random.choice(self.words['custom'])
            scrambled = self.scramble_word(word)
            rounds += 1

            print(f"🔀 Round {rounds}: {scrambled}")
            guess = input("Your guess: ").lower().strip()

            if guess == 'quit':
                print(f"\n📊 Score: {score}/{rounds - 1}")
                return

            if guess == word:
                print("✅ Correct! 🎉")
                score += 1
            else:
                print(f"❌ Wrong! It was: {word}")

            print(f"📊 Score: {score}/{rounds}\n")

    def show_instructions(self):
        """Show how to play"""
        print("\n" + "=" * 50)
        print("📖 HOW TO PLAY")
        print("=" * 50)
        print("""
🎯 OBJECTIVE:
   Unscramble the word to reveal the correct answer!

🎮 CONTROLS:
   • Type your guess and press Enter
   • Type 'quit' to exit to menu
   • In Pro Mode, type 'hint' for a clue

🏆 SCORING:
   • Each correct answer = +1 point
   • Wrong answers = no points
   • Hints cost a hint (limited to 3 per game)

💡 TIPS:
   • Look for common letter patterns
   • Try rearranging the letters in your head
   • Use hints wisely!

📊 MODES:
   1. Classic - Simple unscrambling
   2. Pro - With hints & difficulty levels
   3. Timed - Race against 30 seconds
   4. Multiplayer - Challenge a friend
   5. Custom - Play with your own words

🎨 SPECIAL WORDS:
    paris, vegas, cffa, vintage, gold

   💫 These appear in all modes!
""")
        input("Press Enter to return to menu...")

    def run(self):
        """Main game loop"""
        while True:
            choice = self.choose_mode()

            if choice == '1':
                self.play_classic()
            elif choice == '2':
                self.play_pro_mode()
            elif choice == '3':
                self.play_timed_mode()
            elif choice == '4':
                self.play_multiplayer()
            elif choice == '5':
                self.play_custom_mode()
            elif choice == '6':
                self.show_instructions()
            elif choice == '7':
                print("\n👋 Thanks for playing Word Scramble!")
                print(f"📊 All-time stats: {self.rounds} rounds played")
                break


if __name__ == "__main__":
    game = WordScrambleGame()
    game.run()