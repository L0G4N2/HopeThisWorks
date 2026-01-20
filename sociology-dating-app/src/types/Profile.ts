export interface Profile {
  id: number;
  name: string;
  age: number;
  bio: string;
  interests: string[];
  imageUrl?: string;
}