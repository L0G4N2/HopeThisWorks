import type { Profile } from '../types/Profile';
import '../styles/ProfileCard.css';

interface profileCardProps {
  profile: Profile;
  onLike?: (id: number) => void;
  onPass?: (id: number) => void;
}

function ProfileCard({ profile, onLike, onPass }: profileCardProps) {
  return (
    <div className="profile-card">
      <div className="profile-image-container">
        {profile.imageUrl ? (
          <img src={profile.imageUrl} alt={profile.name} className="profile-image" />
        ) : (
          <div className="profile-image-placeholder">No Image</div>
        )}
      </div>

      <div className="profile-info">
        <h2 className="profile-name">
          {profile.name}, <span className="profile-age">{profile.age}</span>
        </h2>

        <p className="profile-bio">{profile.bio}</p>

        <div className="profile-interests">
          <h3>Interests:</h3>
          <div className="interests-list">
            {profile.interests.map((interest, index) => (
              <span key={index} className="interest-tag">
                {interest}
              </span>
            ))}
          </div>
        </div>
      </div>

      <div className="profile-actions">
        <button
          className="btn btn-pass"
          onClick={() => onPass?.(profile.id)}
          aria-label="Pass on this profile"
        >
          ✕ Pass
        </button>
        <button
          className="btn btn-like"
          onClick={() => onLike?.(profile.id)}
          aria-label="Like this profile"
        >
          ♥ Like
        </button>
      </div>
    </div>
  );
}

export default ProfileCard;