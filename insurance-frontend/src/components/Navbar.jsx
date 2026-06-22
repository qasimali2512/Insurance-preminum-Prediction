import { FaShieldAlt } from "react-icons/fa";

export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="logo">
        <FaShieldAlt />
        <span>InsureAI</span>
      </div>
    </nav>
  );
}