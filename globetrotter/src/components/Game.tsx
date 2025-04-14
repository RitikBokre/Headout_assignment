import React, { useState, useEffect, useCallback } from 'react';
import Confetti from 'react-confetti';
import dataset from '../dataset.json';

interface Destination {
  city: string;
  country: string;
  clues: string[];
  fun_fact: string[];
  trivia: string[];
}

const Game: React.FC = () => {
  const [currentDestination, setCurrentDestination] = useState<Destination | null>(null);
  const [selectedClues, setSelectedClues] = useState<string[]>([]);
  const [options, setOptions] = useState<Destination[]>([]);
  const [score, setScore] = useState({ correct: 0, incorrect: 0 });
  const [showConfetti, setShowConfetti] = useState(false);
  const [gameStatus, setGameStatus] = useState<'playing' | 'correct' | 'incorrect'>('playing');
  const [revealedFact, setRevealedFact] = useState<string>('');

  const getRandomOptions = (correctDestination: Destination) => {
    // Get all cities except the correct one
    const otherCities = dataset.filter(d => d.city !== correctDestination.city);
    
    // Shuffle and get 3 random wrong options
    const wrongOptions = otherCities
      .sort(() => Math.random() - 0.5)
      .slice(0, 3);
    
    // Combine with correct option and shuffle again
    const allOptions = [...wrongOptions, correctDestination]
      .sort(() => Math.random() - 0.5);
    
    return allOptions;
  };

  const selectRandomDestination = useCallback(() => {
    const randomIndex = Math.floor(Math.random() * dataset.length);
    const destination = dataset[randomIndex];
    const randomClues = destination.clues
      .sort(() => Math.random() - 0.5)
      .slice(0, 2);
    
    setCurrentDestination(destination);
    setSelectedClues(randomClues);
    setOptions(getRandomOptions(destination));
    setGameStatus('playing');
    setShowConfetti(false);
    setRevealedFact('');
  }, []);

  useEffect(() => {
    selectRandomDestination();
}, [selectRandomDestination]);

  const handleGuess = (city: string) => {
    if (!currentDestination) return;

    const isCorrect = city === currentDestination.city;
    const randomFact = currentDestination.fun_fact[
      Math.floor(Math.random() * currentDestination.fun_fact.length)
    ];

    setScore(prev => ({
      correct: prev.correct + (isCorrect ? 1 : 0),
      incorrect: prev.incorrect + (isCorrect ? 0 : 1)
    }));

    setGameStatus(isCorrect ? 'correct' : 'incorrect');
    setShowConfetti(isCorrect);
    setRevealedFact(randomFact);
  };

  if (!currentDestination) return <div>Loading...</div>;

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-500 to-purple-600 p-8">
      {showConfetti && <Confetti recycle={false} numberOfPieces={500} />}
      
      <div className="max-w-2xl mx-auto bg-white rounded-xl shadow-2xl p-8">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-800 mb-4">🌍 Globetrotter</h1>
          <div className="flex justify-center gap-4 text-lg">
            <span className="text-green-500">✓ {score.correct}</span>
            <span className="text-red-500">✗ {score.incorrect}</span>
          </div>
        </div>

        <div className="space-y-6">
          {gameStatus === 'playing' && (
            <>
              <div className="space-y-4">
                {selectedClues.map((clue, index) => (
                  <p key={index} className="text-lg text-gray-700 p-4 bg-gray-100 rounded-lg">
                    🤔 {clue}
                  </p>
                ))}
              </div>

              <div className="grid grid-cols-2 gap-4">
                {options.map((destination) => (
                  <button
                    key={destination.city}
                    onClick={() => handleGuess(destination.city)}
                    className="p-4 text-lg bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors"
                  >
                    {destination.city}, {destination.country}
                  </button>
                ))}
              </div>
            </>
          )}

          {gameStatus !== 'playing' && (
            <div className="text-center space-y-6">
              <div className={`text-2xl font-bold ${gameStatus === 'correct' ? 'text-green-500' : 'text-red-500'}`}>
                {gameStatus === 'correct' ? '🎉 Correct!' : <span className="sad-face">😢</span>}
              </div>
              
              <div className="bg-gray-100 p-6 rounded-lg">
                <p className="text-lg text-gray-700">
                  {revealedFact}
                </p>
              </div>

              <button
                onClick={selectRandomDestination}
                className="px-8 py-4 bg-purple-500 text-white rounded-lg hover:bg-purple-600 transition-colors"
              >
                Next Destination
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Game; 