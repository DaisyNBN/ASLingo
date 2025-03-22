import React from "react";
import { Button } from "@/components/ui/button";
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
          Learn sign language the fun and interactive way! Master ASL through bite-sized lessons, challenges, and games.
        </p>
        <div className="flex gap-4 justify-center">
          <Button size="lg">
            <Hand className="mr-2 h-5 w-5" /> Get Started
          </Button>
          <Button variant="outline" size="lg">
            <BookOpen className="mr-2 h-5 w-5" /> Learn More
          </Button>
        </div>
      </motion.div>
      <motion.img 
        src="/sign-language-illustration.png" 
        alt="Sign language illustration" 
        className="mt-12 w-full max-w-md rounded-2xl shadow-lg" 
        initial={{ opacity: 0, y: 20 }} 
        animate={{ opacity: 1, y: 0 }} 
        transition={{ duration: 0.8, delay: 0.3 }}
      />
    </div>
  );
}
