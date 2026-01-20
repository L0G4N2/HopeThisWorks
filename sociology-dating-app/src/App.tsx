import { useState } from 'react'
import ProfileCard from './components/ProfileCard'
import { Profiles } from './data/Profiles'
import './App.css'

function App() {
  const [currentIndex, setCurrentIndex] = useState(0)
  const [likedProfiles, setLikedProfiles] = useState<number[]>([])

  const currentProfile = Profiles[currentIndex]

  const handleLike = (id: number) => {
    setLikedProfiles([...likedProfiles, id])
    goToNextProfile()
  }

  const handlePass = () => {
    goToNextProfile()
  }

  const goToNextProfile = () => {
    if (currentIndex < Profiles.length - 1) {
      setCurrentIndex(currentIndex + 1)
    } else {
      // Loop back to the beginning or show a message
      setCurrentIndex(0)
    }
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>Nexus</h1>
        <p>A Sociology Class Project</p>
      </header>

      <main className="app-main">
        {currentProfile ? (
          <>
            <ProfileCard
              profile={currentProfile}
              onLike={handleLike}
              onPass={handlePass}
            />
            <div className="app-stats">
              <p>Profile {currentIndex + 1} of {Profiles.length}</p>
              <p>Likes: {likedProfiles.length}</p>
            </div>
          </>
        ) : (
          <p>No more profiles to view!</p>
        )}
      </main>
    </div>
  )
}

export default App