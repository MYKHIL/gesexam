
import os

file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Leaderboard Button
nav_target = """            <button onclick="setView('settings')" id="nav-settings" class="px-3 sm:px-4 py-2 text-sm font-medium rounded-lg transition-colors text-gray-700 hover:bg-gray-100">
                Settings
            </button>"""
nav_replacement = """            <button onclick="setView('settings')" id="nav-settings" class="px-3 sm:px-4 py-2 text-sm font-medium rounded-lg transition-colors text-gray-700 hover:bg-gray-100">
                Settings
            </button>
            <button onclick="setView('leaderboard')" id="nav-leaderboard" class="px-3 sm:px-4 py-2 text-sm font-medium rounded-lg transition-colors text-gray-700 hover:bg-gray-100">
                Leaderboard
            </button>"""
content = content.replace(nav_target, nav_replacement)

# 2. Add currentTtsText variable
history_target = "let sessionHistory = []; // Array to store all session scores and timestamps"
history_replacement = """let sessionHistory = []; // Array to store all session scores and timestamps
        let currentTtsText = ""; // Store last text for re-speaking"""
content = content.replace(history_target, history_replacement)

# 3. Update speak function
speak_target = """        function speak(text) {
            const synth = window.speechSynthesis;
            if (!quizSettings.ttsEnabled || !synth || !text) return;

            // Cancel any ongoing speech
            synth.cancel();

            // Remove asterisks for TTS (they're just formatting)
            const cleanText = text.replace(/\*\*/g, '');
            const utterance = new SpeechSynthesisUtterance(cleanText);
            
            // Find the selected voice
            if (quizSettings.ttsVoice) {
                const selectedVoice = voices.find(v => v.voiceURI === quizSettings.ttsVoice);
                if (selectedVoice) {
                    utterance.voice = selectedVoice;
                }
            }
            
            utterance.rate = quizSettings.ttsRate;
            utterance.pitch = quizSettings.ttsPitch;
            
            utterance.onerror = (event) => {
                console.error('SpeechSynthesisUtterance.onerror', event);
                showMessage('An error occurred during speech synthesis.', 'error');
            };

            synth.speak(utterance);

            synth.speak(utterance);
        }"""

speak_replacement = """        function speak(text) {
            currentTtsText = text; // Update current text
            const synth = window.speechSynthesis;
            if (!quizSettings.ttsEnabled || !synth || !text) return;

            // Cancel any ongoing speech
            synth.cancel();

            // Remove asterisks for TTS (they're just formatting)
            const cleanText = text.replace(/\*\*/g, '');
            const utterance = new SpeechSynthesisUtterance(cleanText);
            
            // Find the selected voice
            if (quizSettings.ttsVoice) {
                const selectedVoice = voices.find(v => v.voiceURI === quizSettings.ttsVoice);
                if (selectedVoice) {
                    utterance.voice = selectedVoice;
                }
            }
            
            utterance.rate = quizSettings.ttsRate;
            utterance.pitch = quizSettings.ttsPitch;
            
            utterance.onerror = (event) => {
                console.error('SpeechSynthesisUtterance.onerror', event);
                showMessage('An error occurred during speech synthesis.', 'error');
            };

            synth.speak(utterance);
        }"""
content = content.replace(speak_target, speak_replacement)

# 4. Update toggleTts function
toggle_target = """        function toggleTts() {
            quizSettings.ttsEnabled = !quizSettings.ttsEnabled;
            if (!quizSettings.ttsEnabled) {
                window.speechSynthesis.cancel(); // Stop speech immediately
            }
            saveSettings();
            updateTtsButtons();
            showMessage(`TTS is now ${quizSettings.ttsEnabled ? 'Enabled' : 'Disabled'}.`, 'info');
        }"""
toggle_replacement = """        function toggleTts() {
            quizSettings.ttsEnabled = !quizSettings.ttsEnabled;
            if (!quizSettings.ttsEnabled) {
                window.speechSynthesis.cancel(); // Stop speech immediately
            } else {
                // Re-speak current text if enabled
                if (currentTtsText) {
                    speak(currentTtsText);
                }
            }
            saveSettings();
            updateTtsButtons();
            showMessage(`TTS is now ${quizSettings.ttsEnabled ? 'Enabled' : 'Disabled'}.`, 'info');
        }"""
content = content.replace(toggle_target, toggle_replacement)

# 5. Update displayFeedback function
feedback_target = """        // Updated displayFeedback signature to control TTS
        function displayFeedback(q, selectedOption, feedbackArea, useTts = true) {
            const isCorrect = selectedOption === q.answer;
            const statusClass = isCorrect ? 'bg-green-100 border-green-500 text-green-800' : 'bg-red-100 border-red-500 text-red-800';
            const statusText = isCorrect ? 'Correct!' : 'Incorrect.';
            
            feedbackArea.innerHTML = `
                <div class="p-4 rounded-lg border-l-4 ${statusClass}">
                    <h4 class="font-bold text-lg">${statusText}</h4>
                    <p>The correct answer is <span class="font-extrabold">${q.answer}</span>: ${formatText(q.options[q.answer])}</p>
                    <p class="mt-2 text-sm"><b>Explanation:</b> ${formatText(q.explanation)}</p>
                </div>`;
            feedbackArea.classList.remove('hidden');
            
            if (useTts) {
                let feedbackText = `${statusText} ${q.explanation} so the correct answer is ${q.answer}: ${q.options[q.answer]}.`;
                speak(feedbackText);
            }
        }"""
feedback_replacement = """        // Updated displayFeedback signature to control TTS
        function displayFeedback(q, selectedOption, feedbackArea, useTts = true) {
            const isCorrect = selectedOption === q.answer;
            const statusClass = isCorrect ? 'bg-green-100 border-green-500 text-green-800' : 'bg-red-100 border-red-500 text-red-800';
            const statusText = isCorrect ? 'Correct!' : 'Incorrect.';
            
            feedbackArea.innerHTML = `
                <div class="p-4 rounded-lg border-l-4 ${statusClass}">
                    <h4 class="font-bold text-lg">${statusText}</h4>
                    <p>The correct answer is <span class="font-extrabold">${q.answer}</span>: ${formatText(q.options[q.answer])}</p>
                    <p class="mt-2 text-sm"><b>Explanation:</b> ${formatText(q.explanation)}</p>
                </div>`;
            feedbackArea.classList.remove('hidden');
            
            let feedbackText = `${statusText} ${q.explanation} so the correct answer is ${q.answer}: ${q.options[q.answer]}.`;
            currentTtsText = feedbackText; // Update context

            if (useTts) {
                speak(feedbackText);
            }
        }"""
content = content.replace(feedback_target, feedback_replacement)

# 6. Update renderLeaderboardView and add clearHistory
leaderboard_target = """        function renderLeaderboardView() {
            const historyTableBody = sessionHistory.length === 0 ? 
                '<tr><td colspan="5" class="px-6 py-4 text-center text-gray-500">No sessions yet. Complete a quiz to start tracking history.</td></tr>' :
                sessionHistory.reverse().map((session, index) => {
                    const date = new Date(session.timestamp);
                    const formattedDate = date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
                    const formattedTime = date.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', hour12: true });
                    return `
                        <tr class="border-b hover:bg-gray-100 transition">
                            <td class="px-6 py-4 font-semibold text-gray-700">#${sessionHistory.length - index}</td>
                            <td class="px-6 py-4 text-gray-600">${session.totalQuestions}</td>
                            <td class="px-6 py-4 text-green-600 font-semibold">${session.correctAnswers}</td>
                            <td class="px-6 py-4 text-blue-600 font-bold text-lg">${session.percentage}%</td>
                            <td class="px-6 py-4 text-gray-500 text-sm">${formattedDate} at ${formattedTime}</td>
                        </tr>
                    `;
                }).join('');

            const avgScore = sessionHistory.length > 0 ? 
                (sessionHistory.reduce((sum, s) => sum + s.percentage, 0) / sessionHistory.length).toFixed(1) : 0;
            const bestScore = sessionHistory.length > 0 ? 
                Math.max(...sessionHistory.map(s => s.percentage)) : 0;
            const worstScore = sessionHistory.length > 0 ? 
                Math.min(...sessionHistory.map(s => s.percentage)) : 0;

            contentArea.innerHTML = `
                <div class="p-8 bg-white rounded-xl shadow-lg">
                    <div class="flex justify-between items-center mb-8">
                        <h2 class="text-3xl font-bold text-gray-800">Session History</h2>
                        <button onclick="setView('home')" class="px-4 py-2 bg-gray-600 text-white font-bold rounded-lg hover:bg-gray-700 transition">Back to Home</button>
                    </div>

                    <div class="grid grid-cols-3 gap-4 mb-8">
                        <div class="bg-blue-50 border-l-4 border-blue-500 p-4 rounded-lg">
                            <div class="text-2xl font-bold text-blue-600">${sessionHistory.length}</div>
                            <div class="text-sm text-gray-600">Total Sessions</div>
                        </div>
                        <div class="bg-green-50 border-l-4 border-green-500 p-4 rounded-lg">
                            <div class="text-2xl font-bold text-green-600">${avgScore}%</div>
                            <div class="text-sm text-gray-600">Average Score</div>
                        </div>
                        <div class="bg-purple-50 border-l-4 border-purple-500 p-4 rounded-lg">
                            <div class="text-2xl font-bold text-purple-600">${bestScore}%</div>
                            <div class="text-sm text-gray-600">Best Score</div>
                        </div>
                    </div>

                    <div class="mb-8">
                        <table class="w-full border-collapse border border-gray-300 rounded-lg overflow-hidden">
                            <thead class="bg-blue-600 text-white">
                                <tr>
                                    <th class="px-6 py-3 text-left">Session</th>
                                    <th class="px-6 py-3 text-left">Questions</th>
                                    <th class="px-6 py-3 text-left">Correct</th>
                                    <th class="px-6 py-3 text-left">Score</th>
                                    <th class="px-6 py-3 text-left">Date & Time</th>
                                </tr>
                            </thead>
                            <tbody>
                                ${historyTableBody}
                            </tbody>
                        </table>
                    </div>

                    ${sessionHistory.length > 0 ? `
                        <button onclick="setView('graph')" class="w-full px-6 py-3 bg-indigo-600 text-white font-bold rounded-lg hover:bg-indigo-700 transition">
                            View Progress Graph
                        </button>
                    ` : ''}
                </div>
            `;
        }"""
leaderboard_replacement = """        function renderLeaderboardView() {
            const historyTableBody = sessionHistory.length === 0 ? 
                '<tr><td colspan="5" class="px-6 py-4 text-center text-gray-500">No sessions yet. Complete a quiz to start tracking history.</td></tr>' :
                sessionHistory.reverse().map((session, index) => {
                    const date = new Date(session.timestamp);
                    const formattedDate = date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
                    const formattedTime = date.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', hour12: true });
                    return `
                        <tr class="border-b hover:bg-gray-100 transition">
                            <td class="px-4 sm:px-6 py-4 font-semibold text-gray-700">#${sessionHistory.length - index}</td>
                            <td class="px-4 sm:px-6 py-4 text-gray-600">${session.totalQuestions}</td>
                            <td class="px-4 sm:px-6 py-4 text-green-600 font-semibold">${session.correctAnswers}</td>
                            <td class="px-4 sm:px-6 py-4 text-blue-600 font-bold text-lg">${session.percentage}%</td>
                            <td class="px-4 sm:px-6 py-4 text-gray-500 text-sm whitespace-nowrap">${formattedDate} <span class="hidden sm:inline">at ${formattedTime}</span></td>
                        </tr>
                    `;
                }).join('');

            const avgScore = sessionHistory.length > 0 ? 
                (sessionHistory.reduce((sum, s) => sum + s.percentage, 0) / sessionHistory.length).toFixed(1) : 0;
            const bestScore = sessionHistory.length > 0 ? 
                Math.max(...sessionHistory.map(s => s.percentage)) : 0;

            contentArea.innerHTML = `
                <div class="p-4 sm:p-8 bg-white rounded-xl shadow-lg">
                    <div class="flex flex-col sm:flex-row justify-between items-center mb-8 gap-4">
                        <h2 class="text-2xl sm:text-3xl font-bold text-gray-800">Session History</h2>
                        <div class="flex gap-2">
                             <button onclick="clearHistory()" class="px-4 py-2 bg-red-500 text-white font-bold rounded-lg hover:bg-red-600 transition shadow-md" ${sessionHistory.length === 0 ? 'disabled class="opacity-50 cursor-not-allowed px-4 py-2 bg-red-500 text-white font-bold rounded-lg"' : ''}>Clear History</button>
                             <button onclick="setView('home')" class="px-4 py-2 bg-gray-600 text-white font-bold rounded-lg hover:bg-gray-700 transition shadow-md">Back to Home</button>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-8">
                        <div class="bg-blue-50 border-l-4 border-blue-500 p-4 rounded-lg shadow-sm">
                            <div class="text-2xl font-bold text-blue-600">${sessionHistory.length}</div>
                            <div class="text-sm text-gray-600">Total Sessions</div>
                        </div>
                        <div class="bg-green-50 border-l-4 border-green-500 p-4 rounded-lg shadow-sm">
                            <div class="text-2xl font-bold text-green-600">${avgScore}%</div>
                            <div class="text-sm text-gray-600">Average Score</div>
                        </div>
                        <div class="bg-purple-50 border-l-4 border-purple-500 p-4 rounded-lg shadow-sm">
                            <div class="text-2xl font-bold text-purple-600">${bestScore}%</div>
                            <div class="text-sm text-gray-600">Best Score</div>
                        </div>
                    </div>

                    <div class="mb-8 overflow-x-auto rounded-lg border border-gray-300 shadow-sm">
                        <table class="w-full border-collapse min-w-full">
                            <thead class="bg-blue-600 text-white">
                                <tr>
                                    <th class="px-4 sm:px-6 py-3 text-left text-sm sm:text-base">Session</th>
                                    <th class="px-4 sm:px-6 py-3 text-left text-sm sm:text-base">Qs</th>
                                    <th class="px-4 sm:px-6 py-3 text-left text-sm sm:text-base">Correct</th>
                                    <th class="px-4 sm:px-6 py-3 text-left text-sm sm:text-base">Score</th>
                                    <th class="px-4 sm:px-6 py-3 text-left text-sm sm:text-base">Date</th>
                                </tr>
                            </thead>
                            <tbody class="bg-white">
                                ${historyTableBody}
                            </tbody>
                        </table>
                    </div>

                    ${sessionHistory.length > 0 ? `
                        <button onclick="setView('graph')" class="w-full px-6 py-3 bg-indigo-600 text-white font-bold rounded-lg hover:bg-indigo-700 transition shadow-md">
                            View Progress Graph
                        </button>
                    ` : ''}
                </div>
            `;
        }

        function clearHistory() {
            if (confirm("Are you sure you want to clear your entire session history? This cannot be undone.")) {
                sessionHistory = [];
                localStorage.removeItem(SESSION_HISTORY_KEY);
                renderLeaderboardView();
                showMessage("Session history cleared.", "info");
            }
        }"""
content = content.replace(leaderboard_target, leaderboard_replacement)

# 7. Update renderResults
results_target = """            // Save session to history
            saveSessionToHistory(result.correct, result.total);

            // Speak the appraisal
            speak(appraisal);"""
results_replacement = """            // Save session to history ONLY if all questions were answered
            const answeredCount = Object.keys(userAnswers).length;
            if (answeredCount === result.total) {
                saveSessionToHistory(result.correct, result.total);
            } else {
                console.log("Session not saved: Incomplete quiz.");
            }

            // Speak the appraisal
            speak(appraisal);"""
content = content.replace(results_target, results_replacement)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("File updated successfully.")
