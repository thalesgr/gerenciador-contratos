import React, { useEffect, useState } from 'react';
import Header from '../components/Header';
import ContractTable from '../components/ContractsTables';
import { getContracts } from '../services/services'
import Loading from '../components/Loading';

function Home() {

    return (
        <>
            <ContractTable/>
        </>
    )
}


export default Home