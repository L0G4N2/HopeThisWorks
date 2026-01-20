import type { Profile } from '../types/Profile';
import assets from '../assets/images';

export const Profiles: Profile[] = [
  {
    id: 1,
    imageUrl: assets.AugusteComte,
    name: 'Auguste Comte',
    age: 228,
    bio: 'I could be your daddy 😏',
    interests: ['Sociology', 'Reading', 'Partying'],
  },
  {
    id: 2,
    imageUrl: assets.EmileDurkheim,
    name: 'Emile Durkheim',
    age: 165,
    bio: 'BIG believer in community and social bonds. Looking for someone to share deep conversations with at a nice cafe.',
    interests: ['Sociology', 'Community Service', 'Reading'],
  },
  {
    id: 3,
    imageUrl: assets.KarlMarx,
    name:'Karl Marx',
    age: 206,
    bio: 'Revolutionary at heart. Let\'s overthrow the bourgeoisie together and build a better world!',
    interests: ['Revolution', 'Philosophy', 'Communism', 'Reading'],
  },
  {
    id: 4,
    imageUrl: assets.MaxWeber,
    name: 'Max Weber',
    age: 160,
    bio: 'Analytical thinker who loves to explore the complexities of society. Looking for a partner to discuss ideas and theories with.',
    interests: ['Sociology', 'Philosophy', 'Reading'],
  },
  {
    id: 5,
    imageUrl: assets.W_E_B_DuBois,
    name: 'W.E.B. Du Bois',
    age: 156,
    bio: 'Passionate about social justice and equality. Let\'s make a difference together!',
    interests: ['Social Justice', 'Community Service', 'Reading', 'Traveling', 'Photography'],
  },
  {
    id: 6,
    imageUrl: assets.JaneAddams,
    name: 'Jane Addams',
    age: 164,
    bio: 'Social reformer and advocate for the underprivileged. Looking for someone who shares my passion for making the world a better place!',
    interests: ['Social Reform', 'Community Service', 'Reading', 'Philosophy'],
  }
];