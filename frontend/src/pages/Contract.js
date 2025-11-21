import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { getContractById, saveContract, deleteContract } from '../services/services';
import { Form, Button, Spinner } from 'react-bootstrap';

function Contract() {
  const { id } = useParams(); // se existir, estamos editando
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);
  const [contract, setContract] = useState({
    title: '',
    client: '',
    supplier: '',
    category: '',
    amount: '',
    start_date: '',
    end_date: '',
    status: 'Ativo',
  });

  useEffect(() => {
    const fetchContract = async () => {
      if (id) {
        try {
          console.log("Buscando contrato com id:", id);
          const data = await getContractById(id);
          console.log("Contrato buscado:", data);
          if (data) setContract(data);
        } catch (error) {
          console.error("Erro ao buscar contrato:", error);
        }
      }
      setLoading(false);
    };

    fetchContract();
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setContract(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await saveContract(contract); // serviço que cria/atualiza contrato
      navigate('/'); // voltar para home
    } catch (error) {
      console.error("Erro ao salvar contrato:", error);
    }
  };

   const handleDelete = async () => {
    const confirm = window.confirm("Tem certeza que deseja deletar este contrato?");
    if (!confirm) return;

    try {
      await deleteContract(id);
      navigate('/');
    } catch (error) {
      console.error("Erro ao deletar contrato:", error);
    }
  };

  if (loading) {
    return (
      <div className="d-flex justify-content-center align-items-center" style={{ height: "70vh" }}>
        <Spinner animation="border" role="status" variant="primary">
          <span className="visually-hidden">Loading...</span>
        </Spinner>
      </div>
    );
  }

  return (
    <div className="container my-5">
      <h2 className="mb-4">{id ? 'Editar Contrato' : 'Novo Contrato'}</h2>
      <Form onSubmit={handleSubmit}>
        <Form.Group className="mb-3">
          <Form.Label>Título</Form.Label>
          <Form.Control 
            type="text" 
            name="title" 
            value={contract.title} 
            onChange={handleChange} 
            required 
          />
        </Form.Group>

        <Form.Group className="mb-3">
          <Form.Label>Cliente</Form.Label>
          <Form.Control 
            type="text" 
            name="client" 
            value={contract.client} 
            onChange={handleChange} 
            required 
          />
        </Form.Group>

        <Form.Group className="mb-3">
          <Form.Label>Fornecedor</Form.Label>
          <Form.Control 
            type="text" 
            name="supplier" 
            value={contract.supplier} 
            onChange={handleChange} 
          />
        </Form.Group>

        <Form.Group className="mb-3">
          <Form.Label>Categoria</Form.Label>
          <Form.Control 
            type="text" 
            name="category" 
            value={contract.category} 
            onChange={handleChange} 
          />
        </Form.Group>

        <Form.Group className="mb-3">
          <Form.Label>Valor</Form.Label>
          <Form.Control 
            type="number" 
            name="amount" 
            value={contract.amount} 
            onChange={handleChange} 
            step="0.01" 
          />
        </Form.Group>

        <Form.Group className="mb-3">
          <Form.Label>Data de Início</Form.Label>
          <Form.Control 
            type="date" 
            name="start_date" 
            value={contract.start_date} 
            onChange={handleChange} 
          />
        </Form.Group>

        <Form.Group className="mb-3">
          <Form.Label>Data de Fim</Form.Label>
          <Form.Control 
            type="date" 
            name="end_date" 
            value={contract.end_date} 
            onChange={handleChange} 
          />
        </Form.Group>

        <Form.Group className="mb-3">
          <Form.Label>Status</Form.Label>
          <Form.Select name="status" value={contract.status} onChange={handleChange}>
            <option value="Ativo">Ativo</option>
            <option value="Inativo">Inativo</option>
          </Form.Select>
        </Form.Group>

        <Button variant="primary" type="submit">{id ? 'Salvar Alterações' : 'Criar Contrato'}</Button>
        {id && <Button variant="danger" className="ms-3" onClick={() => handleDelete()}>Deletar Contrato</Button>}
      </Form>
    </div>
  );
}

export default Contract;
