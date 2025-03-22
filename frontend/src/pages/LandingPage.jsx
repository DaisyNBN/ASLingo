import React from "react";
import { motion } from "framer-motion";
import { BookOpen, Hand } from "lucide-react";

export default function LandingPage() {
  return (
    <div className="min-h-screen bg-white flex flex-col items-center justify-center text-center p-6">
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
      >
        <h1 className="text-5xl font-bold mb-4">SignSpeak</h1>
        <p className="text-lg mb-8 max-w-xl">
          Learn sign language the fun and interactive way!
        </p>
        <div className="flex gap-4 justify-center">
          <button className="px-6 py-3 bg-black text-white rounded-xl flex items-center">
            <Hand className="mr-2 h-5 w-5" /> Get Started
          </button>
          <button className="px-6 py-3 border border-black rounded-xl flex items-center">
            <BookOpen className="mr-2 h-5 w-5" /> Learn More
          </button>
        </div>
      </motion.div>
    </div>
  );
}
