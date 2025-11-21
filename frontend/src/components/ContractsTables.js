import React, { useEffect, useState } from 'react';
import { Table, Badge, Button, Form, Row, Col } from 'react-bootstrap';
import Loading from './Loading';
import { getContracts } from '../services/services';
import { useNavigate } from 'react-router-dom';

function ContractTable() {
    const [loading, setLoading] = useState(true);
    const [contracts, setContracts] = useState([]);
    const [pageData, setPageData] = useState();

    const [filters, setFilters] = useState({
        search: '',
        supplier: '',
        category: '',
        status: '',
        min_amount: '',
        max_amount: '',
        start_date: '',
        end_date: '',
        page: 1
    });

    const navigation = useNavigate();

    
    const fetchData = async () => {
        setLoading(true);
        try {
            console.log("Fetching contracts with filters...", filters);
            const data = await getContracts(filters);
            setContracts(data.items);
            setPageData({
                total: data.total,
                page: data.page,
                has_next: data.has_next,
                has_prev: data.has_prev
            });
        } catch (error) {
            console.error("Erro ao buscar contratos:", error);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchData();
    }, [filters.page]);

    const goToDetails = (id) => {
        navigation(`/contracts/${id}`);
    };

    const handleFilterChange = (e) => {
        const { name, value } = e.target;
        setFilters(prev => ({ ...prev, [name]: value, page: 1 })); // reseta página ao alterar filtro
    };

    const applyFilters = () => {
        fetchData();
    };

    const handlePageChange = (type) => {
        setFilters(prev => {
            if (type === 'next' && pageData.has_next) {
                return { ...prev, page: prev.page + 1 };
            } else if (type === 'prev' && pageData.has_prev) {
                return { ...prev, page: prev.page - 1 };
            }
            return prev;
        });
    };

    return (
        <>
            {loading ? <Loading /> : (
                <div className='m-3'>
                    
                    <Form className='mb-3'>
                        <Row className='g-2 d-flex align-items-end'>
                            <Col md={2}>
                                <Form.Control
                                    placeholder="Buscar por contrato ou cliente"
                                    name="search"
                                    value={filters.search}
                                    onChange={handleFilterChange}
                                />
                            </Col>

                            <Col md={2}>
                                <Form.Control
                                    placeholder="Fornecedor"
                                    name="supplier"
                                    value={filters.supplier}
                                    onChange={handleFilterChange}
                                />
                            </Col>

                            <Col md={2}>
                                <Form.Control
                                    placeholder="Categoria"
                                    name="category"
                                    value={filters.category}
                                    onChange={handleFilterChange}
                                />
                            </Col>

                            <Col md={1}>
                                <Form.Select
                                    name="status"
                                    value={filters.status}
                                    onChange={handleFilterChange}
                                >
                                    <option value="">Status</option>
                                    <option value="Ativo">Ativo</option>
                                    <option value="Inativo">Inativo</option>
                                </Form.Select>
                            </Col>

                            <Col md={1}>
                                <Form.Control
                                    type="number"
                                    placeholder="Valor mínimo"
                                    name="min_amount"
                                    value={filters.min_amount}
                                    onChange={handleFilterChange}
                                />
                            </Col>

                            <Col md={1}>
                                <Form.Control
                                    type="number"
                                    placeholder="Valor máximo"
                                    name="max_amount"
                                    value={filters.max_amount}
                                    onChange={handleFilterChange}
                                />
                            </Col>

                            <Col md={1}>
                                <Form.Label className="d-block">Data Início (Período)</Form.Label>
                                <Form.Control
                                    type="date"
                                    name="start_date"
                                    value={filters.start_date}
                                    onChange={handleFilterChange}
                                />
                            </Col>

                            <Col md={1}>
                                <Form.Label className="d-block">Data Fim (Período)</Form.Label>
                                <Form.Control
                                    type="date"
                                    name="end_date"
                                    value={filters.end_date}
                                    onChange={handleFilterChange}
                                />
                            </Col>

                            <Col md={1} className="d-flex align-items-end">
                                <Button onClick={applyFilters} variant="primary" className="w-100">Filtrar</Button>
                            </Col>
                        </Row>
                    </Form>

                    <Table striped bordered hover responsive>
                        <thead className="table-dark">
                            <tr>
                                <th>ID</th>
                                <th>Título</th>
                                <th>Cliente</th>
                                <th>Fornecedor</th>
                                <th>Categoria</th>
                                <th>Valor</th>
                                <th>Data de Início</th>
                                <th>Data de Fim</th>
                                <th>Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            {contracts.map(contract => (
                                <tr key={contract.id} style={{ cursor: "pointer" }} onClick={() => goToDetails(contract.id)}>
                                    <td>{contract.id}</td>
                                    <td>{contract.title}</td>
                                    <td>{contract.client}</td>
                                    <td>{contract.supplier}</td>
                                    <td>{contract.category}</td>
                                    <td>R$ {contract.amount.toLocaleString('pt-BR', { minimumFractionDigits: 2 })}</td>
                                    <td>{contract.start_date}</td>
                                    <td>{contract.end_date}</td>
                                    <td>
                                        <Badge bg={contract.status === "Ativo" ? "success" : "secondary"}>
                                            {contract.status}
                                        </Badge>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </Table>

                    
                    {pageData && (
                        <div className='d-flex justify-content-between align-items-center mt-3'>
                            <strong>Total de Contratos: {pageData.total} </strong>
                            <div className='d-flex align-items-center'>
                                {pageData.has_prev && <Button onClick={() => handlePageChange("prev")} variant="secondary" className="m-3">{"<"}</Button>}
                                <Badge bg="secondary" style={{ height: '40px', width: '30px' }} className='align-items-center d-flex justify-content-center'>
                                    {pageData.page}
                                </Badge>
                                {pageData.has_next && <Button onClick={() => handlePageChange("next")} variant="secondary" className="m-3">{">"}</Button>}
                            </div>
                        </div>
                    )}
                </div>
            )}
        </>
    );
}

export default ContractTable;
