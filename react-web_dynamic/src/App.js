import './App.css';
import CategoryBar from './CategoryBar';
import Devices from './devices';
import Footer from './Footer';
import Header from './Header';
import CategoryItems from './categoryItems'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LeaseDevice from './leaseYourDevice';

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={
          <>
            <CategoryBar />
            <Devices />
          </>
        } />
        <Route path="categories/:id" element={
            <CategoryItems />
        }/>
        <Route path="/lease-my-device" element={
          <LeaseDevice /> 
        }/>

    </Routes>
    <Footer />
    </Router>
  );
}

export default App;
